"""
class BigInt:
----
This class represents an 8 byte integer with a range of -9223372036854775808 to 9223372036854775807
"""


class BigInt:
    def __init__(self, primary=False):
        self.primary = primary
        self.table = None
        self.name = None

    def __name__(self):
        return str(self.name)

    def register_table(self, table, name):
        self.table = table
        self.name = name

