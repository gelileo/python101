import matplotlib.pyplot as plt

# Create a figure with 2 rows and 2 columns of subplots
fig, ax = plt.subplots(2, 2)
fig.suptitle("Multiple Subplots Example")

# Access each subplot using array indexing and plot different data
ax[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16])  # Top-left
ax[0, 1].plot([1, 2, 3, 4], [16, 9, 4, 1])  # Top-right
ax[1, 0].scatter([1, 2, 3, 4], [1, 2, 3, 4])  # Bottom-left
ax[1, 1].bar([1, 2, 3, 4], [1, 3, 2, 5])  # Bottom-right

# Add titles to each subplot
ax[0, 0].set_title("Plot 1")
ax[0, 1].set_title("Plot 2")
ax[1, 0].set_title("Plot 3")
ax[1, 1].set_title("Plot 4")

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Show the figure
plt.show()
