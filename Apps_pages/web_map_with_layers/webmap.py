#Objective : Create a webmap of Volcanoes in the US. Also add features and layers to the map

#Author : Abdul Joheb Ansari

#############################################################################################

import folium
import pandas,io

#Importing volcanoes data and create dataframe object
data = pandas.read_csv("Volcanoes.txt")
data_json = io.open("world.json",'r',encoding='utf-8-sig').read()
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


#function is created here to give certain ranges of elevation certain color
def color_definer(eleva):
    if eleva < 1000:
        return 'green'
    elif 1000 <= eleva  < 3000:
        return 'purple'
    else:
        return 'Red'

#map object is created and  different parameters are passed in Map class for modifying features within the map
#Python code is converted to html code

map = folium.Map(location=[39.56115, -113.294668], zoom_start=5, tiles="OpenStreetMap")

#Now, adding marker to the map using add child method and then pointed to Marker within folium
#Leaflet library is used to create map and then the code is converted  to Javascript 
#Marker is a feature than can have additinal pop up feature
#For example I am passing You are here message to my current location

fg_v = folium.FeatureGroup(name="Volcanoes Layer")

# for i, j in zip([1,2,3], [4,5,6]):
        #print(i, "and",j) and that is equal to 1 and 4 , 2 and 5 and 3, 6 --> zip function allows to do that
    
for latitude,longitude,elevation in zip(lat, lon,elev):
    fg_v.add_child(folium.CircleMarker(location=[latitude,longitude], popup=str(elevation) + "m", 
    fill_color= color_definer(elevation), color = 'grey', fill_opacity =0.8))


fg_p = folium.FeatureGroup(name="Population Layer")

fg_p.add_child(folium.GeoJson(data=data_json,style_function=lambda x: {'fillColor':'green' if x['properties']
['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else
'red' }))

map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())
map.save("Map1.html")





