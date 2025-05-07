# MSFT Revenue & Earnings Chart (Page 2 - Visual)

import matplotlib.pyplot as plt

# Microsoft data from FY2017 to FY2024
years = ['24', '23', '22', '21', '20', '19', '18', '17']
revenue = [245120, 211920, 198270, 168090, 143020, 125840, 110360, 89950]  # in millions
earnings = [88140, 72360, 72740, 61270, 44280, 39240, 16570, 21200]  # in millions
profit_margin = [(e/r)*100 for e, r in zip(earnings, revenue)]  # percentage

fig, ax1 = plt.subplots(figsize=(8, 4))

# Bar chart for Revenue and Earnings
bar_width = 0.35
x = range(len(years))
ax1.bar(x, revenue, bar_width, label='Revenue (Millions)', color='#1f77b4')
ax1.bar([i + bar_width for i in x], earnings, bar_width, label='Earnings (Millions)', color='#ff7f0e')
ax1.set_xlabel('Year')
ax1.set_ylabel('Millions USD')
ax1.set_title('Revenue & Earnings')
ax1.set_xticks([i + bar_width / 2 for i in x])
ax1.set_xticklabels(years)

# Line chart for Profit Margin
ax2 = ax1.twinx()
ax2.plot([i + bar_width / 2 for i in x], profit_margin, label='Profit Margin', color='red', marker='o')
ax2.set_ylabel('Profit Margin (%)')
ax2.set_ylim(0, 50)

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
