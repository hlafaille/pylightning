"""
class Float:
----
This class represents a floating-point number whose precision, at least, n, up to a maximum of 8 bytes.
"""


class Float:
    def __init__(self, precision=2):
        self.precision = precision
        self.table = None
        self.name = None

    def __name__(self):
        return str(self.name)

    def register_table(self, table, name):
        self.table = table
        self.name = name

