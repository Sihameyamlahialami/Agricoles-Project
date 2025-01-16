# Agricoles-Project
# Agricultural Data Analysis and Interactive Dashboard

## Project Overview
This project focuses on integrating, cleaning, analyzing, and visualizing agricultural data from multiple sources. The aim is to provide insights into soil characteristics, historical crop yields, real-time crop monitoring, and meteorological data. The project also includes an interactive dashboard combining spatial and temporal visualizations to aid in decision-making and risk assessment.

---

## Features
1. **Data Integration and Cleaning**
   - Combines soil, crop monitoring, meteorological, and yield history data.
   - Handles missing values, duplicates, and temporal inconsistencies.

2. **Exploratory Data Analysis (EDA)**
   - Statistical summaries for all datasets.
   - Correlation analysis to identify key relationships.

3. **Risk Metrics Calculation**
   - Computes risk indices based on soil properties, crop yields, and environmental factors.
   - Categorizes risk into meaningful levels (e.g., Low, Moderate, High).

4. **Interactive Dashboard**
   - **Bokeh Visualizations**: Temporal trends, NDVI evolution, stress matrix, and yield prediction plots.
   - **Folium Maps**: Spatial heatmaps for risks and parcel-specific data popups.

5. **Prediction and Trend Analysis**
   - Linear regression for yield trends.
   - Seasonal decomposition for NDVI and yield patterns.

---

## Project Structure
```
project_agricole/
├── data/
│   ├── monitoring_cultures.csv       # Real-time crop monitoring data
│   ├── meteo_detaillee.csv           # Hourly meteorological data
│   ├── sols.csv                      # Soil characteristics data
│   ├── historique_rendements.csv     # Historical yield data
├── src/
│   ├── data_manager.py               # Core data management class
│   ├── dashboard.py                  # Bokeh dashboard implementation
│   ├── map_visualization.py          # Folium map visualization implementation
│   ├── report_generator.py           # Automated report generation
├── notebooks/
│   ├── analyses_exploratoires.ipynb  # Jupyter notebook for EDA
├── reports/
│   ├── templates/                    # Templates for automated reporting
│   ├── Rapport_Analyse_Agricole.pdf  # Generated report
└── README.md                         # Project documentation
```

---

## Installation
### Prerequisites
- Python 3.8+
- `pandoc` and `xelatex` for PDF report generation
- At least 8 GB RAM for historical data processing

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project_agricole.git
   cd project_agricole
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
### Data Preparation
1. Place your datasets in the `data/` directory.
2. Ensure the CSV files are formatted correctly as described in the [Project Structure](#project-structure).

### Running the Dashboard
1. Start the Streamlit dashboard:
   ```bash
   streamlit run src/integration_dashboard.py
   ```
2. Open the dashboard in your browser at `http://localhost:8501`.



---

## Key Files
### `data_manager.py`
- Integrates data from multiple sources.
- Provides utilities for cleaning, merging, and feature engineering.

### `dashboard.py`
- Implements Bokeh visualizations for:
  - Yield history trends.
  - NDVI evolution.
  - Stress matrix.
  - Yield predictions.

### `map_visualization.py`
- Uses Folium for:
  - Interactive spatial visualizations.
  - Risk heatmaps.
  - Parcel-specific popups.
  
### `Integration_dashboard.py`
---

## Example Visualizations
### Yield History Plot (Bokeh)
- Displays trends in historical yields for selected parcels.

### NDVI Temporal Plot (Bokeh)
- Shows NDVI evolution over time with historical thresholds.

### Risk Heatmap (Folium)
- Highlights areas with high agricultural risks based on calculated metrics.

---

## Contribution
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.


