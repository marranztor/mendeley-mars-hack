from cartodb import CartoDBAPIKey, CartoDBException

API_KEY ='71cc93154607cf8d7114096ab14c5ab90de92253'
cartodb_domain = 'whereonmars'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
try:
   print(cl.sql('select * from exols_mars_nomenclature'))
except CartoDBException as e:
   print("some error ocurred", e)
