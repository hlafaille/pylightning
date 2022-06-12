"""
class SmallInt:
----
This class represents a 2 byte integer with a range of -32768 to +32767.
"""


class SmallInt:
    def __init__(self):
        self.table = None
        self.name = None

    def __name__(self):
        return str(self.name)

    def register_table(self, table, name):
        self.table = table
        self.name = name

