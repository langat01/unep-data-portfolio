import geopandas as gpd
import matplotlib.pyplot as plt

# Sample data 
protected_areas = gpd.GeoDataFrame({
    "name": ["Nairobi NP", "Ngong Forest"],
    "geometry": gpd.points_from_xy([36.8219, 36.7500], [-1.2921, -1.4000])
}, crs="EPSG:4326")

deforestation = gpd.GeoDataFrame({
    "severity": ["High", "Medium"],
    "geometry": gpd.points_from_xy([36.8219, 36.7400], [-1.2921, -1.4050])
}, crs="EPSG:4326")

# Find overlaps (impact zones)
impact_zones = gpd.sjoin(protected_areas, deforestation, how="inner", predicate="intersects")

# Save and plot
impact_zones.to_file("gef_impact_zones.shp")
impact_zones.plot(figsize=(10, 6), color="green", markersize=100)
plt.title("GEF Impact Zones (Deforestation vs. Protected Areas)")
plt.savefig("impact_map.png")
print("Impact zones saved! Open 'gef_impact_zones.shp' in QGIS.")
