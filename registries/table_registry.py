"""
class TableRegistry:
----
This class keeps track of all tables and their members as a sort of table of contents.
"""


class TableRegistry:
    def __init__(self):
        self.tables = []

    def register_table(self, table):
        self.tables.append({table.__class__.__name__: table._get_columns()})

    def get_table(self, table_name):
        for table in self.tables:
            if table.__class__.__name__ == table_name:
                return table
        else:
            return None
