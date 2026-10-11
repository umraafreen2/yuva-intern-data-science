# Task 5: Analytics Report & Insights Documentation

## Overview
This beginner-friendly project demonstrates a simple sales analysis workflow using Python and Pandas, with charts created using Matplotlib.

**Important:** The included four-row sales dataset is illustrative and hypothetical. It is not real company data.

## Files
- `sample_sales_data.csv` — illustrative product sales dataset
- `sales_analysis.py` — Python script for inspection, summary statistics, findings, and chart creation
- `total_sales_by_product.png` — sales value comparison chart
- `units_sold_by_product.png` — units sold comparison chart

## Tools
- Python
- Pandas
- Matplotlib

## Run the project
1. Install Python 3.
2. Install packages:
   ```bash
   pip install pandas matplotlib
   ```
3. Run from this folder:
   ```bash
   python sales_analysis.py
   ```

The script prints dataset checks and key findings, then saves and displays both charts.

## Findings from the sample data
- Total sales value: ₹2,085.
- Notebook has the highest total sales value: ₹1,000.
- Pen has the highest unit volume: 35 units.
- Units sold and sales value are different measures; both should be considered when interpreting performance.

## Limitations
The dataset contains only four hypothetical products and has no dates, costs, profit margins, or customer information. It is intended for practice only and cannot support conclusions about a real business.
