import csv
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path("01-python-sales-insights/data/sales.csv")
OUT_DIR = Path("01-python-sales-insights/outputs")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def clean_text(x: str) -> str:
    x = (x or "").strip()
    return x if x else "Unknown"

def to_int(x, default=0):
    try:
        return int(x)
    except Exception:
        return default

def to_float(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing dataset: {DATA_PATH}")

    total_revenue = 0.0
    total_qty = 0

    revenue_by_product = defaultdict(float)
    qty_by_product = defaultdict(int)
    revenue_by_city = defaultdict(float)
    revenue_by_channel = defaultdict(float)

    row_count = 0

    with DATA_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            row_count += 1
            product = clean_text(r.get("product"))
            city = clean_text(r.get("city"))
            channel = clean_text(r.get("channel"))
            qty = to_int(r.get("quantity"))
            unit_price = to_float(r.get("unit_price"))

            revenue = qty * unit_price
            total_revenue += revenue
            total_qty += qty

            revenue_by_product[product] += revenue
            qty_by_product[product] += qty
            revenue_by_city[city] += revenue
            revenue_by_channel[channel] += revenue

    summary_path = OUT_DIR / "summary.txt"
    top_product = max(revenue_by_product.items(), key=lambda x: x[1])[0]
    top_city = max(revenue_by_city.items(), key=lambda x: x[1])[0]

    with summary_path.open("w", encoding="utf-8") as f:
        f.write("Sales Insights Summary\n")
        f.write("=====================\n")
        f.write(f"Rows processed: {row_count}\n")
        f.write(f"Total quantity sold: {total_qty}\n")
        f.write(f"Total revenue: {total_revenue:,.2f}\n")
        f.write(f"Top product by revenue: {top_product}\n")
        f.write(f"Top city by revenue: {top_city}\n")

    product_path = OUT_DIR / "product_breakdown.csv"
    with product_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["product", "quantity_sold", "revenue"])
        for p in sorted(revenue_by_product.keys()):
            w.writerow([p, qty_by_product[p], f"{revenue_by_product[p]:.2f}"])

    channel_path = OUT_DIR / "channel_breakdown.csv"
    with channel_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["channel", "revenue"])
        for ch, rev in sorted(revenue_by_channel.items(), key=lambda x: x[1], reverse=True):
            w.writerow([ch, f"{rev:.2f}"])

    print(f"✅ Wrote outputs to: {OUT_DIR}")

if __name__ == "__main__":
    main()
