# Underwriting Vs Investment Income Bar Graph: 

import matplotlib.pyplot as plt

# Simulated example data (in billions)
years = ['2019', '2020', '2021', '2022', '2023']
underwriting_income = [-3.2, 1.5, -2.8, 2.1, -1.7]  # Some years with underwriting losses
investment_income = [6.5, 6.8, 7.2, 7.5, 7.1]       # Steady investment income

x = range(len(years))
bar_width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x, underwriting_income, width=bar_width, label='Underwriting Income', color='salmon')
plt.bar([i + bar_width for i in x], investment_income, width=bar_width, label='Investment Income', color='seagreen')

plt.xlabel('Year')
plt.ylabel('Income (Billions USD)')
plt.title('Underwriting vs Investment Income (P&C Insurers)')
plt.xticks([i + bar_width / 2 for i in x], years)
plt.axhline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('/mnt/data/underwriting_vs_investment_income_bar_chart.png')
plt.show()
