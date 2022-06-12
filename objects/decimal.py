"""
class Decimal:
----
This class represents a variable byte integer with a range up to 131072 digits before the
decimal point; up to 16383 digits after the decimal point.
"""


class Decimal:
    def __init__(self):
        self.table = None
        self.name = None

    def __name__(self):
        return str(self.name)

    def register_table(self, table, name):
        self.table = table
        self.name = name

