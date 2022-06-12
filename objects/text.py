"""
class Text:
---
Represents either a fixed length or unlimited length set of text
"""


class Text:
    def __init__(self):
        self.table = None
        self.name = None

    def __name__(self):
        return str(self.name)

    def register_table(self, table, name):
        self.table = table
        self.name = name

