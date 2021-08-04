#Objective : Create a webmap of Volcanoes in the US. Also add features and layers to the map

#Author : Abdul Joheb Ansari

#############################################################################################

import folium
import pandas

#Importing volcanoes data and create dataframe object
data = pandas.red_csv("Volcanoes.txt")

#map object is created and  different parameters are passed in Map class for modifying features within the map
#Python code is converted to html code

map = folium.Map(location=[36.047, -94.202], zoom_start=7, tiles="Stamen Terrain")

#Now, adding marker to the map using add child method and then pointed to Marker within folium
#Leaflet library is used to convert python code to Javscript when used Marker method
#Marker allows to show pop up information when clicked on the popup icon on the map
#For example I am passing You are here message to my current location

fg = folium.FeatureGroup(name="Extra")
for coordinates in [[36.047, -94.202],[35.047, -94]]:
    fg.add_child(folium.Marker(location=coordinates, popup="You are here", icon=folium.Icon(color='purple')))

map.add_child(fg)


map.save("Map1.html")



