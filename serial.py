"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.curr_num = start

    def generate(self):
        self.curr_num += 1
        return self.curr_num - 1

    def reset(self):
        self.curr_num = self.start