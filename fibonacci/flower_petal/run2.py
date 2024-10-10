import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.cm as cm


def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


# Function to draw the flower with Fibonacci petals
def draw_flower(petals, slider_val):
    # Clear the current plot
    ax.clear()

    # Set up the center of the flower
    center = (0, 0)

    # Calculate the angle for each petal based on the Fibonacci pattern
    end_angle = max((slider_val - 2) // 2, 1) * np.pi
    angles = np.linspace(0, end_angle, petals, endpoint=False)

    # Generate the spiral pattern by using the radius for each petal
    radii = np.arange(1, petals + 1)

    # Plot each petal
    for angle, radius in zip(angles, radii):
        # Use radius to determine the color (normalize radius to [0, 1])
        normalized_radius = (radius - min(radii)) / (max(radii) - min(radii))
        color = colormap(normalized_radius)

        # Adjust the size of the circle representing each petal
        ax.plot(
            [center[0], radius * np.cos(angle)],
            [center[1], radius * np.sin(angle)],
            "o",
            markersize=max(20 - radius // 5, 1),
            color=color,
        )

    # Set title and adjust axis
    ax.set_title(f"Fibonacci Flower with {petals} Petals")
    ax.set_aspect("equal")
    plt.axis("off")

    # Redraw the figure
    plt.draw()


# Update function to redraw the flower based on the slider value
def update(val):
    index = int(petal_slider.val)
    new_petal_count = fib_sequence[index]
    draw_flower(new_petal_count, petal_slider.val)


# Get a colormap
colormap = cm.viridis
max_fibonacci_count = 15
min_fibonacci_count = 3
initial_petal_count = 5

fib_sequence = fibonacci(max_fibonacci_count)

# Create a figure and axis for the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)  # Adjust to fit the slider

# Create a slider for adjusting the number of petals
ax_petal_slider = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
petal_slider = Slider(
    ax_petal_slider,
    "Petals (Index)",
    min_fibonacci_count,
    max_fibonacci_count,
    valinit=initial_petal_count,
    valstep=1,
)

if __name__ == "__main__":
    # Draw the initial flower
    draw_flower(fib_sequence[initial_petal_count], petal_slider.val)

    # Call the update function when the slider's value changes
    petal_slider.on_changed(update)

    plt.show()
