"""
Capstone Project 1: COVID-19 Data Analysis Dashboard
=====================================================
Analyze global COVID-19 trends and produce a multi-panel visualization dashboard.

Usage:
    python starter.py
"""

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
CONFIRMED_URL = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
    "csse_covid_19_data/csse_covid_19_time_series/"
    "time_series_covid19_confirmed_global.csv"
)
DEATHS_URL = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
    "csse_covid_19_data/csse_covid_19_time_series/"
    "time_series_covid19_deaths_global.csv"
)
RECOVERED_URL = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
    "csse_covid_19_data/csse_covid_19_time_series/"
    "time_series_covid19_recovered_global.csv"
)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

TOP_N = 10  # Number of top countries to focus on


# ---------------------------------------------------------------------------
# Step 1: Load Data
# ---------------------------------------------------------------------------
def load_data():
    """Load the three COVID-19 time-series CSVs into DataFrames.

    Returns:
        tuple: (confirmed_df, deaths_df, recovered_df)
    """
    # TODO: Read CSVs using pd.read_csv and return the DataFrames.
    confirmed_df = None
    deaths_df = None
    recovered_df = None
    return confirmed_df, deaths_df, recovered_df


# ---------------------------------------------------------------------------
# Step 2: Clean and Reshape
# ---------------------------------------------------------------------------
def melt_and_clean(df, value_name="cases"):
    """Convert a wide-format JHU DataFrame to long format.

    Steps:
        1. Drop Lat/Long columns.
        2. Group by Country/Region to aggregate provinces.
        3. Melt date columns into rows.
        4. Parse the Date column to datetime.

    Args:
        df (pd.DataFrame): Raw wide-format DataFrame.
        value_name (str): Name for the melted value column.

    Returns:
        pd.DataFrame: Long-format DataFrame with columns
                       [Country, Date, <value_name>].
    """
    # TODO: Implement the cleaning pipeline described above.
    pass


def compute_daily_and_rolling(df, value_col="cases"):
    """Add daily change and 7-day rolling average columns.

    Args:
        df (pd.DataFrame): Long-format DataFrame sorted by Country and Date.
        value_col (str): Column containing cumulative values.

    Returns:
        pd.DataFrame: DataFrame with added 'daily' and 'rolling_7d' columns.
    """
    # TODO: Use groupby + diff for daily values; rolling(7).mean() for smoothing.
    pass


# ---------------------------------------------------------------------------
# Step 3: Exploratory Data Analysis
# ---------------------------------------------------------------------------
def top_countries(df, value_col="cases", n=TOP_N):
    """Return the top-n countries by maximum cumulative value.

    Args:
        df (pd.DataFrame): Long-format DataFrame.
        value_col (str): Column to rank by.
        n (int): Number of countries.

    Returns:
        list[str]: Country names.
    """
    # TODO: Group by country, find max value, sort descending, return top n names.
    pass


def compute_cfr(confirmed_df, deaths_df):
    """Compute Case Fatality Rate by country.

    CFR = total deaths / total confirmed cases * 100

    Returns:
        pd.DataFrame: DataFrame with columns [Country, CFR].
    """
    # TODO: Merge the two DataFrames on Country and compute CFR.
    pass


# ---------------------------------------------------------------------------
# Step 4: Visualizations
# ---------------------------------------------------------------------------
def plot_daily_cases(df, countries, save=True):
    """Line chart of daily new cases for selected countries.

    Args:
        df (pd.DataFrame): Long-format DataFrame with 'rolling_7d' column.
        countries (list[str]): Countries to plot.
        save (bool): Whether to save the figure to disk.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    # TODO: Filter df for given countries, plot rolling_7d vs Date for each.
    ax.set_title("Daily New COVID-19 Cases (7-Day Rolling Average)")
    ax.set_xlabel("Date")
    ax.set_ylabel("New Cases")
    ax.legend()
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "daily_cases.png"), dpi=150)
    plt.show()


def plot_cumulative_area(df, countries, save=True):
    """Stacked area chart of cumulative cases for selected countries."""
    fig, ax = plt.subplots(figsize=(12, 6))
    # TODO: Pivot data and use ax.stackplot or df.plot.area.
    ax.set_title("Cumulative COVID-19 Cases (Top Countries)")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "cumulative_area.png"), dpi=150)
    plt.show()


def plot_deaths_bar(df, countries, save=True):
    """Horizontal bar chart of total deaths by country."""
    fig, ax = plt.subplots(figsize=(10, 6))
    # TODO: Compute total deaths per country, plot horizontal bar chart.
    ax.set_title("Total COVID-19 Deaths by Country")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "deaths_bar.png"), dpi=150)
    plt.show()


def plot_monthly_heatmap(df, countries, save=True):
    """Heatmap of monthly new cases for selected countries."""
    fig, ax = plt.subplots(figsize=(14, 6))
    # TODO: Resample to monthly, pivot to country x month matrix, use sns.heatmap.
    ax.set_title("Monthly New Cases Heatmap")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "monthly_heatmap.png"), dpi=150)
    plt.show()


def plot_dashboard(confirmed, deaths, countries, save=True):
    """Multi-panel dashboard figure combining multiple views."""
    fig, axes = plt.subplots(2, 2, figsize=(18, 12))
    # TODO: Populate each subplot with a different chart type:
    #   axes[0, 0] -- line chart (daily cases)
    #   axes[0, 1] -- bar chart (total deaths)
    #   axes[1, 0] -- heatmap (monthly cases)
    #   axes[1, 1] -- CFR comparison bar chart
    fig.suptitle("COVID-19 Global Dashboard", fontsize=16, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "dashboard.png"), dpi=150)
    plt.show()


# ---------------------------------------------------------------------------
# Step 5: Main Pipeline
# ---------------------------------------------------------------------------
def main():
    """Run the full analysis pipeline."""
    print("Loading data...")
    confirmed_raw, deaths_raw, recovered_raw = load_data()

    print("Cleaning and reshaping...")
    # TODO: Call melt_and_clean for each DataFrame.

    print("Computing daily values and rolling averages...")
    # TODO: Call compute_daily_and_rolling.

    print("Identifying top countries...")
    # TODO: Call top_countries.

    print("Generating visualizations...")
    # TODO: Call each plotting function.

    print("Analysis complete. Figures saved to:", FIGURES_DIR)


if __name__ == "__main__":
    main()
