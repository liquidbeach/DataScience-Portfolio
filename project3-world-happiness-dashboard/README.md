# World Happiness Dashboard Project

This project creates an interactive dashboard visualizing the World Happiness Report 2021 dataset, exploring relationships between happiness scores, GDP per capita, life expectancy, corruption, and regional differences.

## Files
- `world_happiness_dashboard.py`: Python script to load the dataset and create a Plotly dashboard.
- `world-happiness-report-2021.csv`: Dataset containing happiness metrics for various countries.
- `requirements.txt`: List of required Python packages.
- `happiness_dashboard.html`: Output file with the interactive dashboard (generated after running the script).

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   or, if using Conda:
   ```bash
   conda install pandas=2.0.3 plotly=5.22.0 -c conda-forge
   ```
2. Run the script:
   ```bash
   python world_happiness_dashboard.py
   ```
3. A browser window will open with the interactive dashboard. The dashboard is also saved as `happiness_dashboard.html`.

## Results
- Displays four subplots: Happiness vs GDP, Happiness by Region, Happiness vs Life Expectancy, and Happiness vs Corruption.
- Interactive features allow hovering over data points to see country details.