# unep-data-portfolio
Portfolio demo for UNEP GEF Data Analytics Consultant
# 🌍 UNEP GEF Data Analytics Portfolio (Demo)

This repository demonstrates practical solutions aligned with the **UNEP GEF Biodiversity and Land Degradation Unit's** objectives. It simulates a mini-suite of tools that support document management, spatial analysis, and biodiversity reporting—just like those described in the UNEP consultancy Terms of Reference.

---

## 🔧 Contents

### 1. `document_management.py`
A lightweight document management system using **SQLite** to store and organize project documents across the full project lifecycle.
- 📁 Stores titles, types (Proposal, Report, Evaluation), upload dates, and file paths
- 🧪 Includes sample document entries
- 🔍 Supports basic project ID search

### 2. `spatial_impact.py`
A **spatial analysis tool** that detects intersections between protected areas and deforestation points using **GeoPandas**.
- 🗺️ Identifies impact zones where human activity overlaps with conservation targets
- 📤 Outputs a shapefile (`.shp`) and a visualization PNG for use in GIS tools like QGIS

### 3. `biodiversity_dashboard.py`
A **biodiversity data visualization and reporting script** for analyzing GEF project impact across multiple variables.
- 🌿 Tracks species counts, threat levels, project status, and protected area info
- 🗃️ Outputs both CSV and SHP files
- 📊 Generates a color-coded map by threat level

---

## 📂 Outputs

Sample generated files include:
- `biodiversity_data.csv` — clean tabular data for reporting
- `biodiversity_map.shp` — spatial data for GIS
- `biodiversity_map.png` — static visualization map
- `gef_impact_zones.shp` — overlap zones between protected and deforested areas

---

## 🎯 Objective

This demonstration reflects the following UNEP consultancy goals:

- ✅ Improve document archiving and retrieval
- ✅ Support GIS-based spatial monitoring and reporting
- ✅ Enhance visualization of biodiversity project data
- ✅ Synthesize results into reusable, communicable outputs

---

## 🧠 Tools & Libraries Used

- Python 3.10+
- SQLite3
- pandas / geopandas
- matplotlib
- QGIS-compatible shapefiles

---

## 👤 About Me

I am a data management and GIS practitioner with experience in:
- Environmental program monitoring
- Data reporting and visualization
- Spatial data handling
- Knowledge management and documentation

🔗 **LinkedIn / GitHub / CV:** [Your Links Here]

---

## 📬 Contact

If you'd like to collaborate, review this project, or request a demo:
📧 [kipkuruiweldon001@gmail.com]
