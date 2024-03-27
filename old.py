# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# import folium
# import json
# from pyproj import Transformer

# # Initialize the FastAPI app
# app = FastAPI()

# def convert_coordinates(geo_json_data, crs_source, crs_dest="EPSG:4326"):
#     transformer = Transformer.from_crs(crs_source, crs_dest, always_xy=True)
    
#     for feature in geo_json_data['features']:
#         if feature['geometry']['type'] == 'Point':
#             coords = feature['geometry']['coordinates']
#             feature['geometry']['coordinates'] = transformer.transform(coords[0], coords[1])
#         elif feature['geometry']['type'] in ['LineString', 'MultiPoint']:
#             new_coords = [transformer.transform(*coord) for coord in feature['geometry']['coordinates']]
#             feature['geometry']['coordinates'] = new_coords
#         elif feature['geometry']['type'] in ['Polygon', 'MultiLineString']:
#             new_coords = [[transformer.transform(*coord) for coord in ring] for ring in feature['geometry']['coordinates']]
#             feature['geometry']['coordinates'] = new_coords
#         elif feature['geometry']['type'] == 'MultiPolygon':
#             new_coords = [[[transformer.transform(*coord) for coord in ring] for ring in polygon] for polygon in feature['geometry']['coordinates']]
#             feature['geometry']['coordinates'] = new_coords
#     return geo_json_data

# @app.get("/", response_class=HTMLResponse)
# async def read_root():
#     # Load and convert the first geo.json file if necessary
#     geo_json_path_1 = 'geo.json'
#     with open(geo_json_path_1) as f:
#         geo_json_data_1 = json.load(f)

#     # Load and convert the second geo.json file if necessary
#     geo_json_path_2 = 'geo2.json'
#     with open(geo_json_path_2) as f:
#         geo_json_data_2 = json.load(f)
#     geo_json_data_2 = convert_coordinates(geo_json_data_2, "EPSG:32611", "EPSG:4326")

#     # Create a base map, centered around the approximate location of Tijuana
#     map_center = [32.5149, -117.0382]
#     m = folium.Map(location=map_center, zoom_start=12, tiles="CartoDB positron")

#     # Add the GeoJsons to the map
#     folium.GeoJson(
#         geo_json_data_1,
#         name="geojson1",
#         style_function=lambda x: {'color': 'blue', 'weight': 2, 'fillColor': 'grey'},
#         highlight_function=lambda x: {'weight': 3, 'color': 'green'}
#     ).add_to(m)

#     folium.GeoJson(
#         geo_json_data_2,
#         name="geojson2",
#         style_function=lambda x: {'color': 'red', 'weight': 2, 'fillColor': 'orange'},
#         highlight_function=lambda x: {'weight': 3, 'color': 'yellow'}
#     ).add_to(m)

#     # Adding markers for the provided coordinates
#     folium.Marker(
#         [32.538292, -117.071519], 
#         popup='Choque',
#         tooltip='Choque'
#     ).add_to(m)

#     folium.Marker(
#         [32.528875, -117.066432], 
#         popup='Incendio',
#         tooltip='Incendio'
#     ).add_to(m)

#     # Generate map HTML
#     map_html = m._repr_html_()

#     return map_html



