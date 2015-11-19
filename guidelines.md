
## Hack guidelines/notes

Two main activities:

- [Introduction to making a map (of Mars) with CartoDB](#introduction-to-making-a-map-of-mars-with-cartodb)
- [Visualising scientific publications on a map](#visualising-scientific-publications-on-a-map)

#### Introduction to making a map (of Mars) with CartoDB

Learn to create and share maps on the web, and visualize geospatial data using CartoDB.  
Use CartoDB datasets library and/or WhereOnMars datasets.

Reference tutorial: [Making your First Map](http://academy.cartodb.com/courses/beginners-course/making-your-first-map/)

1. Create a cartodb account: http://cartodb.com
2. Find a dataset to visualise (see links below)
3. Create a new map
4. Pick a Mars basemap (see link below)
5. *Have fun creating your viz!*

##### Learning materials

http://academy.cartodb.com  
http://docs.cartodb.com/tutorials  
http://cartodb.github.io/training 

##### Mars datasets

https://github.com/nmanaud/whereonmars/wiki/CartoDB-Datasets  
https://whereonmars.cartodb.com/viz/cd68c630-8be7-11e5-81ea-0ecfd53eb7d3/public_map

##### Mars basemaps

https://github.com/nmanaud/whereonmars/wiki/Basemaps  

#### Visualising scientific publications on a map

Exploring the idea of visualising (Mars-related) scientific publications on a map

1. Download Mars nomenclature: http://planetarynames.wr.usgs.gov/Page/MARS/target
2. Query ADS database: https://ui.adsabs.harvard.edu
3. Query Mendeley database  
4. Build a geo-table containing for each publication the associated location on Mars (point as geom)  
5. Visualise geo-table  
6. What do we see? patterns, issues, new ideas? (e.g.: using Mendeley API to bring a "social layer")  
7. What would make this useful to a researcher?  

##### Mendeley API

http://dev.mendeley.com

##### ADS API

https://pypi.python.org/pypi/ads  
https://github.com/adsabs/adsabs-dev-api  
https://github.com/andycasey/ads

##### CartoDB API

http://docs.cartodb.com/cartodb-platform/sql-api
https://github.com/CartoDB/cartodb-python

*CartoDB SQL API write call example:*

`https://whereonmars.cartodb.com/api/v2/sql?q=INSERT INTO table_name (the_geom, observation) VALUES (ST_GeomFromText(’POINT(-71.2 42.5)’, 4326),'rare bird spotted')&api_key=<API_KEY>`

[Reset API Key](https://whereonmars.cartodb.com/your_apps)
