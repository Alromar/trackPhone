from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key = '9a7a4479d25a473b9714b371bfbf5d3a'
geocoder = OpenCageGeocode(key)

results = geocoder.reverse_geocode(44.8303087, -0.5761911)
pprint(results)
# [{'components': {'ISO_3166-1_alpha-2': 'FR',
#                  'ISO_3166-1_alpha-3': 'FRA',
#                  'ISO_3166-2': ['FR-NAQ', 'FR-33'],
#                  '_category': 'building',
#                  '_type': 'building',
#                  'city': 'Bordeaux',
#                  'continent': 'Europe',
#                  'country': 'France',
#                  'country_code': 'fr',
#                  'county': 'Gironde',
#                  'house_number': '11',
#                  'municipality': 'Bordeaux',
#                  'political_union': 'European Union',
#                  'postcode': '33000',
#                  'region': 'Metropolitan France',
#                  'road': 'Rue Sauteyron',
#                  'state': 'New Aquitaine',
#                  'state_code': 'NAQ',
#                  'suburb': 'Victoire'},
#   'confidence': 10,
#   'formatted': '11 Rue Sauteyron, 33800 Bordeaux, France',
#   'geometry': {'lat': 44.8303087, 'lng': -0.5761911}}]
