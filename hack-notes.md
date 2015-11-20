

Nomenclature dataset:

`https://whereonmars.cartodb.com/tables/exols_mars_nomenclature/public`

`https://whereonmars.cartodb.com/api/v2/sql?q=select feature_name from public.exols_mars_nomenclature`

Output dataset:

`https://whereonmars.cartodb.com/tables/mendeley_mars_hack/table`

`https://whereonmars.cartodb.com/api/v2/sql?q=INSERT INTO mendeley_mars_hack (the_geom, pub_title) VALUES (ST_GeomFromText(’POINT(-71.2 42.5)’, 4326),'Publication title')&api_key=<API_KEY>`


```
from cartodb import CartoDBAPIKey, CartoDBException

API_KEY ='API_KEY'
cartodb_domain = 'whereonmars'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
try:
   print(cl.sql('select * from exols_mars_nomenclature'))
except CartoDBException as e:
   print("some error ocurred", e)

```
