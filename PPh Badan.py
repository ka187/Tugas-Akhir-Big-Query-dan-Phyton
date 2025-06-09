# Calculate total tax liability for each scenario
total_tax_normal = df_normal['tax_liability_normal'].sum()
total_tax_holiday = df_holiday['tax_liability_holiday'].sum()
total_tax_depreciation = df_depreciation['tax_liability_depreciation'].sum()

# Create a DataFrame for comparison
df_comparison = pd.DataFrame({
    'Scenario': ['Normal Tax', 'Tax Holiday', 'Depreciation (Declining Balance)'],
    'Total Tax Liability': [total_tax_normal, total_tax_holiday, total_tax_depreciation]
})

# Visualize Perbandingan Total PPh Badan antar Skenario
plt.figure(figsize=(8, 6))
plt.bar(df_comparison['Scenario'], df_comparison['Total Tax Liability'], color=['skyblue', 'lightgreen', 'orange'])
plt.title('Comparison of Total PPh Badan Across Scenarios', fontsize=14)
plt.xlabel('Scenario', fontsize=12)
plt.ylabel('Total PPh Badan', fontsize=12)
plt.grid(axis='y')
plt.savefig('total_tax_comparison.png')
plt.show()

# Visualize Grafik 3d PPh Badan By Tahun
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Assuming 'tahun' and 'tax_liability_normal' are available in df_normal
ax.scatter(df_normal['tahun'], df_normal['pendapatan'], df_normal['tax_liability_normal'], c='skyblue', marker='o')

ax.set_xlabel('Tahun', fontsize=12)
ax.set_ylabel('Pendapatan', fontsize=12)
ax.set_zlabel('PPh Badan (Normal Scenario)', fontsize=12)
plt.title('3D Scatter Plot of PPh Badan by Tahun and Pendapatan (Normal Scenario)', fontsize=14)
plt.savefig('3d_tax_tahun.png')
plt.show()

# Calculate straight-line depreciation tax liability for comparison
df_merged['depreciation_straight_line'] = df_merged['nilai_perolehan'] / df_merged['umur_ekonomis']
df_merged['tax_liability_straight_line'] = (df_merged['pendapatan'] - df_merged['depreciation_straight_line']) * df_merged['tax_rate']

# Visualize Grafik Perbandingan PPh Badan dari Waktu ke Waktu: Penyusutan Garis Lurus vs Saldo Menurun
plt.figure(figsize=(10, 6))
plt.plot(df_merged['tahun'], df_merged['tax_liability_straight_line'], marker='o', linestyle='-', color='purple', label='Garis Lurus')
plt.plot(df_merged['tahun'], df_merged['tax_liability_depreciation'], marker='o', linestyle='-', color='orange', label='Saldo Menurun') # Using previously calculated declining balance
plt.title('Comparison of PPh Badan Over Time: Straight Line vs Declining Balance Depreciation', fontsize=14)
plt.xlabel('Tahun', fontsize=12)
plt.ylabel('PPh Badan', fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig('depreciation_method_comparison.png')
plt.show()