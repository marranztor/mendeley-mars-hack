

Nomenclature dataset:
https://whereonmars.cartodb.com/tables/exols_mars_nomenclature/public

https://whereonmars.cartodb.com/api/v2/sql?q=SELECT feature_name public.exols_mars_nomenclature

Output dataset;
https://whereonmars.cartodb.com/tables/mendeley_mars_hack/table

`https://whereonmars.cartodb.com/api/v2/sql?q=INSERT INTO mendeley_mars_hack (the_geom, pub_title) VALUES (ST_GeomFromText(’POINT(-71.2 42.5)’, 4326),'Publication title')&api_key=<API_KEY>`

