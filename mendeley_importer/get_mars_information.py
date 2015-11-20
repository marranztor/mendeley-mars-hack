#!/usr/bin/python

from cartodb import CartoDBAPIKey, CartoDBException
from mendeley import Mendeley
import requests
import sys
import yaml

def render_authors(authors):
    authors_list = []
    for author in authors:
        authors_list.append("%s %s" % (author.first_name, author.last_name))

    return "; ".join(authors_list)

def get_list_features():
    features = []
    r = requests.get("https://whereonmars.cartodb.com/api/v2/sql?q=SELECT%20feature_name,%20the_geom%20from%20public.exols_mars_nomenclature").json()

    for feature in r['rows']:
        features.append(feature)

    return features

def query_documents(session, feature):
    feature = "\"%s\" AND mars" % (feature)
    search = session.catalog.search(feature)
    page = search.list()

    documents = []

    count = 0
    for document in page.items:
        authors=render_authors(document.authors)
        print authors
        print "Title:",document.title,"Year:",document.year

        d = {}

        d['year'] = document.year
        d['authors'] = render_authors(document.authors)
        d['title'] = document.title
        d['link'] = document.link
        # d['reader_count'] = document.reader_count

        documents.append(d)
        count += 1

        if count > 5:
            break

    return documents

def insert_documents(cl, feature_name, the_geom, documents):
    for d in documents:
        try:
            sql = "INSERT INTO mendeley_mars_hack (feature_name, link, the_geom, title, authors, year) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (feature_name, d['link'], the_geom, d['title'], d['authors'], d['year'])
            sql = sql.encode('ascii', 'ignore')
            print sql
            cl.sql(sql)
            print "Done!"
        except CartoDBException as e:
            print "some error ocurred", e

def main():
    with open('config.yml') as f:
        config = yaml.load(f)

    mendeley = Mendeley(config['mendeleyId'], config['mendeleySecret'])
    session = mendeley.start_client_credentials_flow().authenticate()
    features = get_list_features()

    cl = CartoDBAPIKey(config['cartodbSecret'], config['cartodbDomain'])

    cl.sql("DELETE FROM mendeley_mars_hack")

    for feature in features:
        documents = query_documents(session, feature['feature_name'])
        insert_documents(cl, feature['feature_name'], feature['the_geom'], documents)

if __name__ == "__main__":
    main()
