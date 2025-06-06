import matplotlib.pyplot as plt
import numpy as np

# Years from 2038 to 2046
years = np.arange(2038, 2047)

# Scenario A: 10% depreciation in 2039, then 2% appreciation annually
# Assumes inflation rises due to depreciation, then gradually falls
inflation_sg_a = [6.0, 8.5, 4, 3.2, 2.1, 0.8, -0.5, 0.3, 0.9]
inflation_laos_a = [6.0, 9.1, 3.8, 2.9, 3.3, 3.5, 3.2, 2.8, 2.5]

# Scenario B: Flat NEER to 2045, 1% appreciation after
# Assumes inflation stabilizes or slowly decreases
inflation_sg_b = [6.0, 4.8, 4.0, 3.4, 2.9, 2.5, 2.6, 2.1, 1.8]
inflation_laos_b = [6.0, 5.2, 4.4, 3.9, 3.2, 2.7, 2.4, 2.0, 1.5]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, inflation_sg_a, label="Singapore - Scenario A", linestyle='-', marker='o', color='red')
plt.plot(years, inflation_laos_a, label="Laos - Scenario A", linestyle='--', marker='o', color='orange')
plt.plot(years, inflation_sg_b, label="Singapore - Scenario B", linestyle='-', marker='s', color='blue')
plt.plot(years, inflation_laos_b, label="Laos - Scenario B", linestyle='--', marker='s', color='green')

plt.title("Projected Inflation Paths (2038–2046): Scenario A vs. B")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("inflation_paths_sg_laos.png")
plt.show()

# This code generates a plot comparing the projected inflation rates for Singapore and Laos under two different scenarios from 2038 to 2046.
# The inflation rates are hypothetical and illustrate how different economic scenarios can affect inflation trends.
# The plot is saved as 'inflation_paths_sg_laos.png'.
# This is a comment. It will not print(anything).
print("This is not a comment.") # Although this is
print("This ")