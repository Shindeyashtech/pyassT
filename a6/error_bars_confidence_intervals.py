import numpy as np
import matplotlib.pyplot as plt

# Sample data: average heights of two groups with confidence intervals
groups = ['Group A', 'Group B']
means = [5.6, 5.8]  # average heights in feet
ci_lower = [5.4, 5.6]
ci_upper = [5.8, 6.0]

# Calculate error bars (distance from mean to lower and upper bounds)
error_lower = np.array(means) - np.array(ci_lower)
error_upper = np.array(ci_upper) - np.array(means)
asymmetric_error = [error_lower, error_upper]

# Plot bar chart with asymmetric error bars
fig, ax = plt.subplots(figsize=(6,4))
bars = ax.bar(groups, means, yerr=asymmetric_error, capsize=10, color='skyblue', edgecolor='black', error_kw=dict(ecolor='red', lw=2))

ax.set_ylabel('Average Height (feet)')
ax.set_title('Average Height with 95% Confidence Intervals')

# Customize error bars: red color, line width 2, cap size 10
# If error bars overlap, means are not significantly different

plt.show()

# Additional example: scatter plot with error bars

# Sample data points with errors
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.0, 2.5, 3.7, 3.2, 4.8])
yerr = np.array([0.2, 0.3, 0.15, 0.4, 0.25])

plt.figure(figsize=(6,4))
plt.errorbar(x, y, yerr=yerr, fmt='o', ecolor='green', elinewidth=2, capsize=5, capthick=2, markerfacecolor='blue', markersize=8)
plt.title('Scatter Plot with Error Bars')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
