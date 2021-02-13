import folium
import pandas

DataSource = pandas.read_csv("Volcanoes_USA.txt")
lat = list(DataSource["LAT"])
lon = list(DataSource["LON"])
elev = list(DataSource["ELEV"])
name = list(DataSource["NAME"])

def mag_elevation(m_el):
    if m_el < 1800:
        return 'green'
    elif 1800 <= m_el < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.60, -99.10], zoom_start=6, tiles="OpenStreetMap")

fg = folium.FeatureGroup("My Map")

for lt,ln,el,nm in zip(lat,lon,elev,name):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=8, popup=nm, fill_color=mag_elevation(el), color='black', fill_opacity=0.9))

fg.add_child(folium.GeoJson(data=open('coordinates.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'filColor':'yellow'}))

map.add_child(fg)

map.save("My_map.html")

