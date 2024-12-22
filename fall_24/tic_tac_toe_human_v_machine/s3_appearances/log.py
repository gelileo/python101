class Logger:
    def __init__(self, debug=False):
        self.debug = debug

    def log(self, *args):
        if self.debug:
            print(*args)
