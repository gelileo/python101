import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QSlider,
    QPushButton,
    QLabel,
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# Fibonacci sequence generator
def fibonacci(n):
    fib_seq = [1, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


# Create a class that handles the Matplotlib figure and canvas
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)

    def draw_spiral(self, num_segments):
        self.ax.clear()

        # Set up the Fibonacci sequence
        fib_seq = fibonacci(num_segments)

        # Starting parameters for drawing the spiral
        x, y = 0, 0  # Starting point
        width, height = fib_seq[0], fib_seq[0]  # Initial square size
        angle = 0  # Start angle (0 degrees)

        for i, r in enumerate(fib_seq):
            # Draw the square based on the current angle
            if angle == 0:  # Moving right
                square = plt.Rectangle((x, y), r, r, fill=None, edgecolor="black")
                x += r
            elif angle == 90:  # Moving up
                square = plt.Rectangle((x - r, y), r, r, fill=None, edgecolor="black")
                y += r
            elif angle == 180:  # Moving left
                square = plt.Rectangle(
                    (x - r, y - r), r, r, fill=None, edgecolor="black"
                )
                x -= r
            elif angle == 270:  # Moving down
                square = plt.Rectangle((x, y - r), r, r, fill=None, edgecolor="black")
                y -= r

            # Add the square to the plot
            self.ax.add_patch(square)

            # Label the square with the Fibonacci number
            self.ax.text(
                x - r / 2, y - r / 2, str(r), fontsize=12, ha="center", va="center"
            )

            # Correct the arc placement: The arc should be drawn from the correct corner
            if angle == 0:  # Arc starts from the bottom left corner
                arc_x_center, arc_y_center = x - r, y
            elif angle == 90:  # Arc starts from the bottom right corner
                arc_x_center, arc_y_center = x, y - r
            elif angle == 180:  # Arc starts from the top right corner
                arc_x_center, arc_y_center = x + r, y
            elif angle == 270:  # Arc starts from the top left corner
                arc_x_center, arc_y_center = x, y + r

            # Draw the quarter arc inside the square
            theta = np.linspace(np.radians(angle), np.radians(angle + 90), 100)
            arc_x = arc_x_center + r * np.cos(theta)
            arc_y = arc_y_center + r * np.sin(theta)
            self.ax.plot(arc_x, arc_y, color="blue")

            # Update the angle for the next square and arc
            angle = (angle + 90) % 360

        # Set the aspect ratio to 'equal' for a uniform spiral
        self.ax.set_aspect("equal")
        self.ax.set_title(f"Fibonacci Spiral with {num_segments} segments")
        self.draw()

    def display_nature_image(self, image_path):
        try:
            self.ax.clear()
            img = plt.imread(image_path)
            self.ax.imshow(img)
            self.ax.axis("off")  # Hide axes for nature mode
            self.draw()
        except Exception as e:
            print(f"Error displaying image: {e}")


# Main window class for the game
class FibonacciSpiralGame(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Fibonacci Spiral Drawing Game")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        layout = QVBoxLayout()

        # Add a Matplotlib canvas for drawing the Fibonacci spiral
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        # Label to show the current number of segments
        self.label = QLabel(f"Number of segments: 5", self)
        layout.addWidget(self.label)

        # Slider for controlling the number of Fibonacci segments
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(3)
        self.slider.setMaximum(10)  # Increase to allow for larger terms
        self.slider.setValue(5)
        self.slider.valueChanged.connect(self.update_spiral)
        layout.addWidget(self.slider)

        # Button to toggle "Nature Mode"
        self.nature_button = QPushButton("Nature Mode", self)
        self.nature_button.clicked.connect(self.toggle_nature_mode)
        layout.addWidget(self.nature_button)

        # Set up the central widget and layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initial drawing
        self.in_nature_mode = False
        self.update_spiral()

    def update_spiral(self):
        if self.in_nature_mode:
            self.exit_nature_mode()

        num_segments = self.slider.value()
        self.label.setText(f"Number of segments: {num_segments}")
        self.canvas.draw_spiral(num_segments)

    def toggle_nature_mode(self):
        if not self.in_nature_mode:
            self.enter_nature_mode()
        else:
            self.exit_nature_mode()

    def enter_nature_mode(self):
        self.in_nature_mode = True
        self.nature_button.setText("Exit Nature Mode")
        # Display nature images related to Fibonacci spirals
        self.canvas.display_nature_image("nature_fibonacci.jpg")  # Example image path

    def exit_nature_mode(self):
        self.in_nature_mode = False
        self.nature_button.setText("Nature Mode")
        self.update_spiral()


# Main entry point
def main():
    app = QApplication(sys.argv)
    window = FibonacciSpiralGame()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
