"""
Task 5: Analytics Report & Insights Documentation
Note: This is an educational example using illustrative sales data, not real business records.
Run: python sales_analysis.py
Required packages: pandas, matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "sample_sales_data.csv"
df = pd.read_csv(data_path)

# Basic data inspection
print("Dataset preview:")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nMissing values per column:")
print(df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Calculate total sales if it is not already present
if "Total_Sales_INR" not in df.columns:
    df["Total_Sales_INR"] = df["Units_Sold"] * df["Unit_Price_INR"]

print("\nSummary statistics:")
print(df[["Units_Sold", "Unit_Price_INR", "Total_Sales_INR"]].describe())

# Key findings
total_revenue = df["Total_Sales_INR"].sum()
top_revenue_product = df.loc[df["Total_Sales_INR"].idxmax(), "Product"]
top_volume_product = df.loc[df["Units_Sold"].idxmax(), "Product"]

print(f"\nTotal sales across all products: ₹{total_revenue:,.0f}")
print(f"Highest sales value: {top_revenue_product}")
print(f"Highest unit volume: {top_volume_product}")

# Chart 1: Total sales by product
plt.figure(figsize=(7, 4.5))
plt.bar(df["Product"], df["Total_Sales_INR"])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (INR)")
plt.tight_layout()
plt.savefig(BASE_DIR / "total_sales_by_product.png", dpi=160)
plt.show()

# Chart 2: Units sold by product
plt.figure(figsize=(7, 4.5))
plt.bar(df["Product"], df["Units_Sold"])
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig(BASE_DIR / "units_sold_by_product.png", dpi=160)
plt.show()
