import folium
import json

map = folium.Map(location=[37.574187, 126.976882], zoom_start=15) 

with open('./week6/data/skorea-provinces-2018-geo.json') as f:
    text = f.read()
d = json.loads(text)
folium.GeoJson(d, name='json_data').add_to(map)

map.show_in_browser()