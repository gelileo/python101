import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QComboBox,
    QSizePolicy,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# Create a class that handles the Matplotlib figure and canvas
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)

    def recreate_canvas(self, polar=False):
        """Recreate the figure and axes, optionally as a polar plot."""
        self.fig.clear()  # Clear the figure
        if polar:
            self.ax = self.fig.add_subplot(111, polar=True)  # Polar plot
        else:
            self.ax = self.fig.add_subplot(111)  # Cartesian plot
        self.draw()  # Redraw the canvas


# Create the main window for the app
class ChartDemoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Chart Demo App")
        self.setGeometry(100, 100, 800, 600)

        # Main layout using QGridLayout for custom positioning
        layout = QGridLayout()

        # Combo box to select the chart type
        self.combo = QComboBox(self)
        self.combo.addItems(
            [
                "Histogram",
                "Pie Chart",
                "Box Plot",
                "Heatmap",
                "Area Plot",
                "Contour Plot",
                "Quiver Plot",
                "Polar Plot",
                "Stem Plot",
            ]
        )

        # Set the size policy to control the width (half of the canvas width)
        self.combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # layout.addWidget(self.combo)
        # Connect combo box selection change to the show_chart function
        self.combo.currentIndexChanged.connect(self.show_chart)

        # Add combo box to layout (top-left corner, taking up half the width)
        layout.addWidget(self.combo, 0, 0, 1, 2)  # Row 0, Col 0-1 (2 columns wide)

        # Matplotlib canvas
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas, 1, 0, 1, 4)  # Row 1, spanning 4 columns

        # Set row stretch factors to control spacing
        layout.setRowStretch(0, 0)  # No extra space above the combo box
        layout.setRowStretch(1, 1)  # Allow the canvas to expand

        # Set column stretch factors to control horizontal layout
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        # Create a container for the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Show the initial chart (default selection)
        self.show_chart()

    def show_chart(self):
        chart_type = self.combo.currentText()  # Get selected chart type

        # Switch between polar and cartesian axes based on the selected chart
        if chart_type == "Polar Plot":
            self.canvas.recreate_canvas(polar=True)  # Recreate canvas with polar plot
        else:
            self.canvas.recreate_canvas(polar=False)  # Use regular cartesian plot

        if chart_type == "Histogram":
            data = np.random.randn(1000)
            self.canvas.ax.hist(data, bins=30, color="skyblue", edgecolor="black")
            self.canvas.ax.set_title("Histogram")
            self.canvas.ax.set_xlabel("Value")
            self.canvas.ax.set_ylabel("Frequency")

        elif chart_type == "Pie Chart":
            labels = ["Apples", "Bananas", "Cherries", "Dates"]
            sizes = [25, 35, 20, 20]
            colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
            self.canvas.ax.pie(
                sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90
            )
            self.canvas.ax.set_title("Pie Chart")
            self.canvas.ax.axis("equal")

        elif chart_type == "Box Plot":
            data = [np.random.normal(0, std, 100) for std in range(1, 4)]
            self.canvas.ax.boxplot(data, vert=True, patch_artist=True)
            self.canvas.ax.set_title("Box Plot")
            self.canvas.ax.set_ylabel("Values")

        elif chart_type == "Heatmap":
            data = np.random.rand(10, 10)
            cax = self.canvas.ax.imshow(data, cmap="hot", interpolation="nearest")
            self.canvas.figure.colorbar(cax)
            self.canvas.ax.set_title("Heatmap")

        elif chart_type == "Area Plot":
            x = np.linspace(0, 10, 100)
            y1 = np.sin(x)
            y2 = np.cos(x)
            self.canvas.ax.fill_between(x, y1, color="skyblue", alpha=0.5, label="Sine")
            self.canvas.ax.fill_between(
                x, y2, color="lightgreen", alpha=0.5, label="Cosine"
            )
            self.canvas.ax.set_title("Area Plot")
            self.canvas.ax.legend()

        elif chart_type == "Contour Plot":
            x = np.linspace(-5, 5, 100)
            y = np.linspace(-5, 5, 100)
            X, Y = np.meshgrid(x, y)
            Z = np.sin(np.sqrt(X**2 + Y**2))
            self.canvas.ax.contour(X, Y, Z, levels=20, cmap="RdGy")
            self.canvas.ax.set_title("Contour Plot")

        elif chart_type == "Quiver Plot":
            x = np.arange(0, 5, 1)
            y = np.arange(0, 5, 1)
            X, Y = np.meshgrid(x, y)
            U = np.cos(X)
            V = np.sin(Y)
            self.canvas.ax.quiver(X, Y, U, V)
            self.canvas.ax.set_title("Quiver Plot")

        elif chart_type == "Polar Plot":
            theta = np.linspace(0, 2 * np.pi, 100)
            r = np.abs(np.sin(2 * theta) * np.cos(2 * theta))
            self.canvas.ax.plot(theta, r)
            self.canvas.ax.set_title("Polar Plot")

        elif chart_type == "Stem Plot":
            x = np.linspace(0, 2 * np.pi, 10)
            y = np.sin(x)
            self.canvas.ax.stem(x, y)
            self.canvas.ax.set_title("Stem Plot")

        # Redraw the canvas with the updated plot
        self.canvas.draw()


# Main entry point
def main():
    app = QApplication(sys.argv)
    window = ChartDemoApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
