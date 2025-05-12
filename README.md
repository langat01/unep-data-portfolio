# 🌍 UNEP GEF Data Analytics Portfolio (Demo)

This repository demonstrates practical solutions aligned with the **UNEP GEF Biodiversity and Land Degradation Unit's** objectives. It simulates a mini-suite of tools that support document management, spatial analysis, and biodiversity reporting — similar to those outlined in the UNEP consultancy Terms of Reference.

---

## 🔧 Contents

### 1. `document_management.py`
A lightweight document management system using **SQLite** to organize documents across the full project lifecycle.
- 📁 Stores titles, types (Proposal, Report, Evaluation), upload dates, and file paths
- 🧪 Includes sample document entries
- 🔍 Supports basic project ID search

### 2. `spatial_impact.py`
A **spatial analysis tool** that detects intersections between protected areas and deforestation points using **GeoPandas**.
- 🗺️ Identifies impact zones where human activity overlaps with conservation targets
- 📤 Outputs a shapefile (`.shp`) and a visualization PNG for GIS tools like QGIS

### 3. `biodiversity_dashboard.py`
A **biodiversity data visualization and reporting tool** to analyze GEF project impact across various ecological indicators.
- 🌿 Tracks species counts, threat levels, project status, and protected area info
- 🗃️ Outputs both CSV and SHP files
- 📊 Generates a color-coded map by threat level

---

## 📂 Sample Outputs

- `biodiversity_data.csv` — clean tabular data for reporting
- `biodiversity_map.shp` — spatial data for GIS
- `biodiversity_map.png` — threat-level visualization map
- `gef_impact_zones.shp` — zones where conservation areas intersect with deforestation

---

## 📸 Sample Output

![Biodiversity Threat Map](biodiversity_map.png)

---

## 🚀 How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/langat01/unep-data-portfolio.git
cd unep-data-portfolio
