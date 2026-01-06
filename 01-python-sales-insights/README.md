# Project 01 — Python Sales Insights

This project reads a CSV file, cleans messy values, calculates sales metrics, and exports results.

## What this project does
- Loads raw sales data from a CSV file
- Cleans missing and dirty text values
- Converts numeric fields from text to numbers
- Calculates total sales quantity and total revenue
- Aggregates revenue by product, city, and sales channel
- Exports clean, reusable output files

## Project structure
- data/ — raw input data (CSV)
- src/ — Python analysis code
- outputs/ — generated results (text and CSV files)

## How to run the project
From the repository root:

Activate the virtual environment:
source .venv/bin/activate

Run the analysis script:
python 01-python-sales-insights/src/analyze_sales.py

## Outputs
- outputs/summary.txt — high-level sales summary
- outputs/product_breakdown.csv — quantity and revenue by product
- outputs/channel_breakdown.csv — revenue by sales channel
