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
        """create serial number with starting number"""
        self.start = start
        self.initial_start = start

    def __repr__(self):
        return f"SerialGenerator start = {self.start}"

    def generate(self):
        """on the first call, return the start value.
            On later calls, add one to previos serial number and return it"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """reset the serial number to the start value and return None"""
        self.start = self.initial_start
    
