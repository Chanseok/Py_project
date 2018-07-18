
# Googple Maps API Key
# AIzaSyCV4UkHA4SHXRfriYrSHt3x2ASbTnszpRc

#%%
import googlemaps
from datetime import datetime
#from googlemaps import Client

gmaps_key = "AIzaSyCV4UkHA4SHXRfriYrSHt3x2ASbTnszpRc"
gmaps = googlemaps.Client(key=gmaps_key)

geocode_result = gmaps.geocode('서울중부경찰서', language='ko')
geocode_result
geocode_result[0]['formatted_address']

