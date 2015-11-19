
## Hack guidelines/notes


#### A) Introduction to CartoDB

Learn how to quickly create a map visualisation using Carto DB.
Using Mars data (or Earth)

- [ ] create a cartodb account
- [ ] find a dataset to visualise
- [ ] create a new map
- [ ] pick a Mars basemap
- [ ] have fun creating your viz!

**Links**

http://academy.cartodb.com  
http://docs.cartodb.com/tutorials  
http://cartodb.github.io/training  
https://github.com/nmanaud/whereonmars/wiki/Basemaps  
https://github.com/nmanaud/whereonmars/wiki/CartoDB-Datasets  
https://whereonmars.cartodb.com/viz/cd68c630-8be7-11e5-81ea-0ecfd53eb7d3/public_map

#### B) Visualising scientific publications on a map

- [ ] download nomenclature  
- [ ] query Mendeley database  
- [ ] query ADS database  
- [ ] build a geo-table containing for each publication the associated location on Mars (point as geom)  
- [ ] visualise geo-table  
- [ ] what do we see? patterns, issues, new ideas? (e.g.: using Mendeley API to bring a "social layer")  
- [ ] what would make this useful to a researcher?  

##### ADS API

https://pypi.python.org/pypi/ads  
https://github.com/adsabs/adsabs-dev-api  
https://github.com/andycasey/ads/  

##### CartoDB API

http://docs.cartodb.com/cartodb-platform/sql-api/
https://github.com/CartoDB/cartodb-python

*CartoDB SQL API write call example:*

`https://whereonmars.cartodb.com/api/v2/sql?q=INSERT INTO table_name (the_geom, observation) VALUES (ST_GeomFromText(’POINT(-71.2 42.5)’, 4326),'rare bird spotted')&api_key=<API_KEY>`

[Reset API Key](https://whereonmars.cartodb.com/your_apps)
