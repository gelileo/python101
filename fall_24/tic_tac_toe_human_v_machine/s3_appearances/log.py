class Logger:
    def __init__(self, debug=False):
        self.debug = debug

    def log(self, *args):
        """
        Print the arguments to the console if debug is enabled.
        """
        if self.debug:
            print(*args)
