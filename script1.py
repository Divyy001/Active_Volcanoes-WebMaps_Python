import folium
import pandas as pd
map = folium.Map(location=[38.58, -99.09], zoom_start= 5, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
df1 = pd.read_csv("4.1 Volcanoes.txt.txt")
lat = list(df1['LAT'])
lon = list(df1['LON'])
name = list(df1["NAME"])
eleva = list(df1['ELEV'])

def color_chnge(el):
    if el>2000:
        return 'green'
    else:
        return 'blue'

html = """<h4>Volcano Info<h4>
 name:<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br> 
elevation: %s m 
"""
for lt, lg, nme, el in zip(lat,lon,name,eleva):
    iframe = folium.IFrame(html=html %(nme,nme,el), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt,lg],popup=folium.Popup(iframe), icon=folium.Icon(color_chnge(el))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open("13.1 world.json.json", 'r', encoding='utf-8-sig').read()),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")