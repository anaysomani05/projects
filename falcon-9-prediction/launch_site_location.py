import folium
import wget
import pandas as pd
from folium.plugins import MarkerCluster, MousePosition
from folium.features import DivIcon
import webbrowser

# Download and read the `spacex_launch_geo.csv`
spacex_csv_file = wget.download('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv')
spacex_df = pd.read_csv(spacex_csv_file)

# Select relevant sub-columns: `Launch Site`, `Lat(Latitude)`, `Long(Longitude)`, `class`
spacex_df = spacex_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long', 'class']]
print(launch_sites_df)

# Start location is NASA Johnson Space Center
nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=5)

# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
# Create a blue circle at NASA Johnson Space Center's coordinate with an icon showing its name
marker = folium.map.Marker(
    nasa_coordinate,
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
    )
)
site_map.add_child(circle)
site_map.add_child(marker)

# For each launch site, add a Circle object based on its coordinate (Lat, Long) values. In addition, add Launch site name as a popup label
for i in range(len(launch_sites_df.index)):
    coordinate = [launch_sites_df["Lat"][i], launch_sites_df["Long"][i]]
    circle = folium.Circle(coordinate, radius=100, color='#d35400', fill=True).add_child(folium.Popup(launch_sites_df["Launch Site"][i]))
    marker = folium.map.Marker(
        coordinate,
        icon=DivIcon(
            icon_size=(20,20),
            icon_anchor=(0,0),
            html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % launch_sites_df["Launch Site"][i],
        )
    )
    site_map.add_child(circle)
    site_map.add_child(marker)

# Save the map to an HTML file
site_map.save('spacex_launch_sites.html')

# Open the HTML file in the default web browser
webbrowser.open('spacex_launch_sites.html')

print(spacex_df.tail(10))
marker_cluster = MarkerCluster()
print(launch_sites_df)

def func(item):
    if item == 1:
        return 'green'
    else:
        return 'red'

launch_sites_df["marker_color"] = launch_sites_df["class"].apply(func)
print(launch_sites_df)

# Function to assign color to launch outcome
def assign_marker_color(launch_outcome):
    if launch_outcome == 1:
        return 'green'
    else:
        return 'red'
    
spacex_df['marker_color'] = spacex_df['class'].apply(assign_marker_color)
print(spacex_df.tail(10))

# Add Mouse Position to get the coordinate (Lat, Long) for a mouse over on the map
formatter = "function(num) {return L.Util.formatNum(num, 5);};"
mouse_position = MousePosition(
    position='topright',
    separator=' Long: ',
    empty_string='NaN',
    lng_first=False,
    num_digits=20,
    prefix='Lat:',
    lat_formatter=formatter,
    lng_formatter=formatter,
)

site_map.add_child(mouse_position)

from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

lat1 = 34.632834
lon1 = -120.610746
lat2 = 34.63494
lon2 = -120.62429

distance_railway = calculate_distance(lat1, lon1, lat2, lon2)

# Create and add a folium.Marker on your selected closest railway point on the map
coordinate = [34.63494, -120.62429]
icon_ = folium.DivIcon(html=str(round(distance_railway, 2)) + " km")
marker = folium.map.Marker(
    coordinate,
    icon=icon_
)
marker.add_to(site_map)

# Create a `folium.PolyLine` object using the railway point coordinate and launch site coordinate
railway = [34.63494, -120.62429]
launch = [34.632834, -120.610746]
line = folium.PolyLine([railway, launch])
site_map.add_child(line)

# Save the updated map to an HTML file
site_map.save('spacex_launch_sites_updated.html')

# Open the updated HTML file in the default web browser
webbrowser.open('spacex_launch_sites_updated.html')