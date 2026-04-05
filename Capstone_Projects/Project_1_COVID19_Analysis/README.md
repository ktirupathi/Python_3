# Capstone Project 1: COVID-19 Data Analysis Dashboard

## Objective

Build a comprehensive data analysis pipeline that explores global COVID-19 trends, visualizes
key metrics across countries, and produces an interactive-style dashboard using Python's
data visualization libraries. By the end of this project you will be comfortable loading
real-world messy data, cleaning it, performing exploratory data analysis (EDA), and
communicating insights through publication-quality charts.

---

## Skills Practiced

| Skill | Library |
|---|---|
| Data loading and cleaning | Pandas |
| Exploratory Data Analysis | Pandas, NumPy |
| Static visualizations | Matplotlib, Seaborn |
| Dashboard-style multi-panel figures | Matplotlib subplots |
| Time-series analysis | Pandas datetime |

---

## Dataset

**Source:** Johns Hopkins University CSSE COVID-19 Dataset (public, updated daily during the pandemic).

| File | URL |
|---|---|
| Confirmed cases | `https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv` |
| Deaths | `https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv` |
| Recovered | `https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv` |

You can load these directly with `pd.read_csv(url)`.

---

## Step-by-Step Instructions

### Step 1 -- Load and Inspect the Data
- Read all three CSV files into DataFrames.
- Examine shapes, column names, data types, and missing values.
- Understand the wide-format layout (dates as columns).

### Step 2 -- Clean and Reshape
- Melt the wide-format DataFrames into long format with columns: `Country`, `Date`, `Value`.
- Parse the `Date` column to `datetime`.
- Aggregate province-level rows to country-level totals.
- Handle missing or inconsistent country names.

### Step 3 -- Exploratory Data Analysis
- Compute daily new cases and deaths from cumulative totals.
- Calculate 7-day rolling averages to smooth out reporting noise.
- Identify the top 10 most-affected countries by total confirmed cases and deaths.
- Compute case fatality rates (CFR) by country.

### Step 4 -- Visualizations
Create at least the following charts:

1. **Line chart** -- Daily new cases over time for the top 5 countries.
2. **Stacked area chart** -- Cumulative cases for the top 10 countries.
3. **Bar chart** -- Total deaths by country (top 15).
4. **Heatmap** -- Monthly new cases for selected countries using Seaborn.
5. **Multi-panel dashboard** -- A single figure with 4+ subplots summarizing the pandemic.

### Step 5 -- Insights and Reporting
- Write a short narrative (in code comments or markdown cells) summarizing:
  - Which countries were hit hardest and when?
  - How did waves differ across regions?
  - What does the CFR tell us (and what are its limitations)?

---

## Expected Deliverables

1. `starter.py` (or Jupyter notebook) with complete, well-commented analysis code.
2. At least 5 saved chart images (PNG) in a `figures/` subdirectory.
3. A brief written summary of findings (as comments, docstrings, or a markdown section).

---

## Bonus Challenges

- Add a **choropleth world map** using `plotly.express` to show cases geographically.
- Build a simple **Streamlit** or **Panel** dashboard that lets users pick a country and date range interactively.
- Perform **correlation analysis** between COVID-19 severity and external indicators (population density, GDP per capita) by merging in a second dataset.
- Forecast future cases for a selected country using a simple ARIMA or Prophet model.
- Compare vaccination rollout speed across countries by incorporating the Our World in Data vaccination dataset.
