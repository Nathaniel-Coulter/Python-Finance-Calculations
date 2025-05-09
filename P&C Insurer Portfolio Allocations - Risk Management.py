# P&C Portfolio - Risk Management graph 2:

import matplotlib.pyplot as plt

# Data
labels = ['Bonds', 'Common Stock', 'Cash & Short-Term', 'Real Estate', 'Preferred Stock', 'Other']
sizes = [62.55, 13, 5.65, 1.21, 0.78, 8.45]
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0', '#ffb3e6']

# Plot
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    sizes,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85
)

# Add a legend (key) to the side
plt.legend(wedges, labels, title="Asset Classes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('P&C Insurer Investment Allocation')
plt.axis('equal')  # Equal aspect ratio keeps the pie chart round
plt.tight_layout()

# Save and display
plt.savefig('/mnt/data/pc_insurer_investment_pie_chart_readable.png')
plt.show()
