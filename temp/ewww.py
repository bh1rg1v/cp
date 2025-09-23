import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample OHLC data
dates = pd.date_range("2025-08-22", periods=5, freq="B")
np.random.seed(42)
prices = np.random.randint(24500, 25000, size=(5,))

ohlc_data = pd.DataFrame({
    "Date": dates,
    "Day": dates.strftime("%A"),
    "Open": prices,
    "High": prices + np.random.randint(50, 200, size=5),
    "Low": prices - np.random.randint(50, 200, size=5),
    "Close": prices + np.random.randint(-100, 100, size=5),
})

# Remove timestamp
ohlc_data["Date"] = ohlc_data["Date"].dt.strftime("%Y-%m-%d")

# Create figure
fig, ax = plt.subplots(figsize=(8, 2))
ax.axis("off")

# ✅ Draw table WITHOUT index/row numbers
tbl = ax.table(cellText=ohlc_data.values, colLabels=ohlc_data.columns,
               loc="center", cellLoc="center")

# Style
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)

# Color first and last day's close cyan with labels
tbl[(1, 5)].set_facecolor('cyan')
tbl[(1, 5)].get_text().set_text(f"{ohlc_data.iloc[0]['Close']} (A)")
tbl[(5, 5)].set_facecolor('cyan')
tbl[(5, 5)].get_text().set_text(f"{ohlc_data.iloc[4]['Close']} (B)")

# Find highest in High column (column 2) and lowest in Low column (column 3)
high_max_idx = ohlc_data['High'].idxmax() + 1  # +1 for header row
low_min_idx = ohlc_data['Low'].idxmin() + 1    # +1 for header row

# Color highest High and lowest Low light green with labels
tbl[(high_max_idx, 3)].set_facecolor('lightgreen')
tbl[(high_max_idx, 3)].get_text().set_text(f"{ohlc_data.iloc[high_max_idx-1]['High']} (C)")
tbl[(low_min_idx, 4)].set_facecolor('lightgreen')
tbl[(low_min_idx, 4)].get_text().set_text(f"{ohlc_data.iloc[low_min_idx-1]['Low']} (D)")

# Calculate values
A = ohlc_data.iloc[0]['Close']
B = ohlc_data.iloc[4]['Close']
C = ohlc_data.iloc[high_max_idx-1]['High']
D = ohlc_data.iloc[low_min_idx-1]['Low']
absolute_change = abs(B - A)
change1 = abs(C - A)
change2 = abs(D - A)
max_peak_change = max(change1, change2)

# Add texts aligned to left
fig.text(0.1, 0.15, f'Absolute Change = |B - A| = {absolute_change}', ha='left', fontsize=10)
fig.text(0.1, 0.10, f'Peak Change1 = |C - A| = {change1}', ha='left', fontsize=10)
fig.text(0.1, 0.07, f'Peak Change2 = |D - A| = {change2}', ha='left', fontsize=10)
fig.text(0.1, 0.04, f'Max Peak Change = max(Change1, Change2) = {max_peak_change}', ha='left', fontsize=10)

plt.show()