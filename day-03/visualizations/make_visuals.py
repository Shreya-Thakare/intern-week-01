"""
Day 3 - Visualization Script
Facility Hygiene Dataset (cleaned)

Produces:
  1. bar_avg_cleanliness_by_location.png   (bar chart)
  2. bar_hygiene_risk_distribution.png     (bar chart)
  3. hist_cleanliness_score.png            (histogram)
  4. scatter_odor_vs_complaints.png        (scatter plot)
  5. heatmap_feature_correlation.png       (additional visualization)
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

CLEAN_CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "facility_hygiene_cleaned.csv")
OUT_DIR = os.path.dirname(__file__)

plt.rcParams.update({"figure.dpi": 120, "font.size": 10})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, name), bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {name}")


def main():
    df = pd.read_csv(CLEAN_CSV_PATH)

    # 1. Bar chart — average cleanliness score by location
    avg_clean = df.groupby("location")["cleanliness_score"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(avg_clean.index, avg_clean.values, color="#3B82F6")
    ax.set_xlabel("Average Cleanliness Score (0-10)")
    ax.set_title("Average Cleanliness Score by Location")
    ax.set_xlim(0, 10)
    for i, v in enumerate(avg_clean.values):
        ax.text(v + 0.05, i, f"{v:.2f}", va="center", fontsize=9)
    save(fig, "bar_avg_cleanliness_by_location.png")

    # 2. Bar chart — hygiene risk distribution
    risk_order = ["Low", "Medium", "High"]
    risk_counts = df["hygiene_risk"].value_counts().reindex(risk_order)
    colors = ["#22C55E", "#F59E0B", "#EF4444"]
    fig, ax = plt.subplots(figsize=(6, 5))
    bars = ax.bar(risk_counts.index, risk_counts.values, color=colors)
    ax.set_ylabel("Number of Facilities")
    ax.set_title("Hygiene Risk Distribution")
    for bar, v in zip(bars, risk_counts.values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 5, str(v), ha="center", fontsize=10)
    save(fig, "bar_hygiene_risk_distribution.png")

    # 3. Histogram — cleanliness score distribution
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(df["cleanliness_score"], bins=20, color="#6366F1", edgecolor="white")
    ax.axvline(df["cleanliness_score"].mean(), color="black", linestyle="--", label=f"Mean = {df['cleanliness_score'].mean():.2f}")
    ax.set_xlabel("Cleanliness Score (0-10)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Cleanliness Scores")
    ax.legend()
    save(fig, "hist_cleanliness_score.png")

    # 4. Scatter plot — odor score vs. complaints, colored by risk
    fig, ax = plt.subplots(figsize=(7, 5))
    color_map = {"Low": "#22C55E", "Medium": "#F59E0B", "High": "#EF4444"}
    for risk, color in color_map.items():
        subset = df[df["hygiene_risk"] == risk]
        ax.scatter(subset["odor_score"], subset["complaints"], s=18, alpha=0.6, color=color, label=risk)
    ax.set_xlabel("Odor Score (0-10)")
    ax.set_ylabel("Number of Complaints")
    ax.set_title("Odor Score vs. Complaints by Hygiene Risk")
    ax.legend(title="Hygiene Risk")
    save(fig, "scatter_odor_vs_complaints.png")

    # 5. Additional visualization — correlation heatmap
    num_cols = ["cleanliness_score", "odor_score", "waste_level", "footfall", "complaints", "hours_since_cleaning"]
    corr = df[num_cols].corr()
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(num_cols)))
    ax.set_yticks(range(len(num_cols)))
    ax.set_xticklabels(num_cols, rotation=45, ha="right")
    ax.set_yticklabels(num_cols)
    for i in range(len(num_cols)):
        for j in range(len(num_cols)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center",
                     color="white" if abs(corr.iloc[i, j]) > 0.5 else "black", fontsize=8)
    ax.set_title("Feature Correlation Heatmap")
    fig.colorbar(im, ax=ax, shrink=0.8)
    save(fig, "heatmap_feature_correlation.png")


if __name__ == "__main__":
    main()
