import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from datetime import datetime

# Simulated GEF Biodiversity/Land Degradation project data
data = {
    "project_id": ["BD-001", "BD-002", "LD-003"],
    "project_title": ["Habitat Restoration", "Community Forests", "Soil Regeneration"],
    "protected_area": ["Nairobi NP", "Ngong Forest", "Kereita Forest"],
    "species_count": [150, 89, 42],
    "threat_level": ["HIGH", "MEDIUM", "LOW"],
    "area_ha": [1200, 540, 760],
    "status": ["Implementation", "Reporting", "Closure"],
    "start_year": [2020, 2021, 2019],
    "end_year": [2024, 2023, 2022],
    "latitude": [-1.2921, -1.4000, -1.5000],
    "longitude": [36.8219, 36.7500, 36.6000]
}

# Create DataFrame and convert to GeoDataFrame
df = pd.DataFrame(data)
df["duration_years"] = df["end_year"] - df["start_year"]
df["reporting_year"] = datetime.now().year

gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df.longitude, df.latitude),
    crs="EPSG:4326"
)

# Export tabular and spatial data
df.to_csv("biodiversity_data.csv", index=False)
gdf.to_file("biodiversity_map.shp")

# Visualization
ax = gdf.plot(
    figsize=(10, 6),
    column="threat_level",
    cmap="coolwarm",
    legend=True,
    markersize=100,
    alpha=0.7
)
for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf["project_id"]):
    ax.text(x + 0.01, y + 0.01, label, fontsize=9)
plt.title("GEF Project Sites: Biodiversity & Land Degradation (Sample Data)")
plt.tight_layout()
plt.savefig("biodiversity_map.png")

print(" All outputs saved: biodiversity_data.csv, biodiversity_map.shp, biodiversity_map.png")
