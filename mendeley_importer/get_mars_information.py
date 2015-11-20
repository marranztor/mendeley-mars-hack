#!/usr/bin/python

from mendeley import Mendeley
import yaml

def render_authors(authors):
    authors_list = []
    for author in authors:
        authors_list.append(author.first_name+", "+author.last_name)

    return "; ".join(authors_list)

def main():
    with open('config.yml') as f:
        config = yaml.load(f)

    mendeley = Mendeley(config['mendeleyId'], config['mendeleySecret'])
    session = mendeley.start_client_credentials_flow().authenticate()

    title = "mars"

    search = session.catalog.search(title)
    page = search.list()
    for document in page.items:
        authors=render_authors(document.authors)
        print authors
        print "Title:",document.title,"Year:",document.year

if __name__ == "__main__":
    main()
