# make_data_day1_from_csv.py
# Atsumi2025_airtemp_7days.csv から 2025-08-24 のデータを読み取り、
# data_day1.py を自動生成するスクリプト
import csv

CSV_PATH = "Atsumi2025_airtemp_7days.csv"
TARGET_DATE = "2025-08-24"

temps = []

# ★ encoding を utf-8-sig に変更
with open(CSV_PATH, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Date"] == TARGET_DATE:
            value = float(row["Air Temp (°C)"])
            temps.append(value)

with open("data_day1.py", "w", encoding="utf-8") as f:
    f.write("# 自動生成されたデータファイル\n")
    f.write(f"# source: {CSV_PATH}, date={TARGET_DATE}\n\n")
    f.write("temperatures = [\n")
    for t in temps:
        f.write(f"    {t:.2f},\n")
    f.write("]\n")

print("data_day1.py を生成しました。")
