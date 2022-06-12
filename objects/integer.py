"""
class Integer:
----
This class represents a 4 byte integer with a range of -2147483648 to +2147483647.
"""


class Integer:
    def __init__(self):
        self.table = None
        self.name = None

    def __name__(self):
        return str(self.name)

    def register_table(self, table, name):
        self.table = table
        self.name = name

