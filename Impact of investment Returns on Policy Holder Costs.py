#Impact of investment Returns on Policy Holder Costs 

import matplotlib.pyplot as plt

# Hypothetical example: effect of investment returns on premium pricing
investment_returns = [2, 4, 6, 8]  # % return
premium_reduction = [5, 10, 15, 20]  # % cost reduction due to investment yield

plt.figure(figsize=(8, 5))
plt.plot(investment_returns, premium_reduction, marker='o', linestyle='-', color='royalblue')
plt.title('Impact of Investment Returns on Policyholder Premiums')
plt.xlabel('Investment Return (%)')
plt.ylabel('Potential Premium Reduction (%)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(investment_returns)
plt.yticks(range(0, 25, 5))

plt.tight_layout()
plt.savefig('/mnt/data/investment_return_vs_premium_reduction.png')
plt.show()
