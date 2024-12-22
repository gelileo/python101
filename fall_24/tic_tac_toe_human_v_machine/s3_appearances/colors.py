class Colors:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (64, 128, 255, 160)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200, 128)
    DARK_GRAY = (128, 128, 128)  # Darker color for hover effect
    GLOW_COLOR = (255, 255, 0)  # Yellow for glow effect

    def __init__(self, mode="light"):
        self.mode = mode
        self.set_colors()

    def set_colors(self):
        if self.mode == "light":
            self.BG_COLOR = self.WHITE
            self.LINE_COLOR = self.BLUE
            self.CIRCLE_COLOR = self.RED
            self.CROSS_COLOR = self.BLACK
            self.BUTTON_COLOR = self.GRAY
            self.BUTTON_TEXT_COLOR = self.BLUE
            self.BUTTON_COLOR_HOVER = self.DARK_GRAY
            self.BUTTON_TEXT_COLOR_HOVER = self.WHITE
            self.CIRCLE_PULSE_COLOR = (255, 150, 150)  # Light red
            self.CROSS_PULSE_COLOR = (150, 150, 150)  # Light gray
        else:
            self.BG_COLOR = (10, 10, 30)  # Dark blue background
            self.LINE_COLOR = (50, 150, 255)  # Glowing blue for grid
            self.CIRCLE_COLOR = (200, 0, 0)  # Glowing red for O
            self.CROSS_COLOR = (0, 200, 0)  # Glowing green for X
            self.BUTTON_COLOR = (50, 50, 50)
            self.BUTTON_TEXT_COLOR = (200, 200, 200)
            self.BUTTON_COLOR_HOVER = (100, 100, 100)
            self.BUTTON_TEXT_COLOR_HOVER = (255, 255, 255)
            self.CIRCLE_PULSE_COLOR = (255, 50, 50)  # Bright red
            self.CROSS_PULSE_COLOR = (50, 255, 50)  # Bright green
