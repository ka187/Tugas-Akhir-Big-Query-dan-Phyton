# --- Setup ---
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set seed agar hasil bisa direproduksi
np.random.seed(42)

# --- 1. Daftar Obat ---
items = [
    {"item_id": f"OBT{str(i).zfill(3)}", "item_name": f"Obat_{i}", "unit": "tablet"} 
    for i in range(1, 21)
]

# --- 2. Tabel Persediaan Farmasi ---
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='MS')
inventory_data = []

for date in dates:
    for item in items:
        qty = np.random.randint(100, 500)
        purchase_price = round(np.random.uniform(1000, 5000), 2)
        selling_price = round(purchase_price * np.random.uniform(1.2, 1.5), 2)
        inventory_data.append({
            "date": date.strftime('%Y-%m-%d'),
            "item_id": item["item_id"],
            "item_name": item["item_name"],
            "unit": item["unit"],
            "quantity_purchased": qty,
            "purchase_price_per_unit": purchase_price,
            "selling_price_per_unit": selling_price,
            "total_cost": round(qty * purchase_price, 2)
        })

df_inventory = pd.DataFrame(inventory_data)

# --- 3. Tabel Pemakaian Obat Rawat Inap (Menggunakan FIFO) ---
inpatient_usage = []

for _ in range(1000):
    date = datetime.strptime("2023-01-01", "%Y-%m-%d") + timedelta(days=np.random.randint(0, 365))
    item = random.choice(items)
    qty_used = np.random.randint(1, 10)
    
    try:
        cost = df_inventory[(df_inventory["item_id"] == item["item_id"]) & 
                            (pd.to_datetime(df_inventory["date"]) <= date)].sort_values(by="date").iloc[0]["purchase_price_per_unit"]
    except IndexError:
        cost = 2000  # fallback value
    
    inpatient_usage.append({
        "date": date.strftime('%Y-%m-%d'),
        "item_id": item["item_id"],
        "item_name": item["item_name"],
        "quantity_used": qty_used,
        "cost_per_unit": cost,
        "total_cost": round(qty_used * cost, 2)
    })

df_inpatient = pd.DataFrame(inpatient_usage)

# --- 4. Tabel Penjualan Obat Rawat Jalan (Apotik) ---
outpatient_sales = []

for _ in range(1200):
    date = datetime.strptime("2023-01-01", "%Y-%m-%d") + timedelta(days=np.random.randint(0, 365))
    item = random.choice(items)
    qty_sold = np.random.randint(1, 10)
    
    try:
        sell_price = df_inventory[(df_inventory["item_id"] == item["item_id"]) & 
                                  (pd.to_datetime(df_inventory["date"]) <= date)].sort_values(by="date").iloc[0]["selling_price_per_unit"]
    except IndexError:
        sell_price = 3000  # fallback value
    
    outpatient_sales.append({
        "date": date.strftime('%Y-%m-%d'),
        "item_id": item["item_id"],
        "item_name": item["item_name"],
        "quantity_sold": qty_sold,
        "selling_price_per_unit": sell_price,
        "total_sales": round(qty_sold * sell_price, 2)
    })

df_outpatient = pd.DataFrame(outpatient_sales)

# --- 5. Simpan sebagai CSV ---
df_inventory.to_csv("tabel_persediaan_farmasi.csv", index=False)
df_inpatient.to_csv("tabel_pemakaian_obat_rawat_inap.csv", index=False)
df_outpatient.to_csv("tabel_penjualan_obat_rawat_jalan.csv", index=False)

print("✅ Dataset berhasil dibuat dan disimpan sebagai file CSV di direktori kerja saat ini.")
