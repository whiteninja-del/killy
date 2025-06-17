import json

#load geojson file
with open("museums.geojson") as f:
    geojson_data=json.load(f)

#print basic info
print(geojson_data.values())  

#access features
features=geojson_data["features"]
print(features[2])