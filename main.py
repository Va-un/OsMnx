import folium
import matplotlib.pyplot as plt
from branca.element import Figure

fig3= Figure(width=550,height=350)
m3=folium.Map(location=[12.84243, 80.06048],tiles='cartodbpositron',zoom_start=11)
fig3.add_child(m3)

#Adding markers to the map
folium.Marker(location=[12.84034, 80.06176],popup='Default popup Marker1',tooltip='Click here to see Popup').add_to(m3)
folium.Marker(location=[12.84386, 80.05971],popup='<strong>Marker3</strong>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)


m3.save('aee.html')

