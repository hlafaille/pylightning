"""
class Join:
----
This class represents the physical action of doing a JOIN in SQL databases.
"""


class Join:
    LEFT_JOIN = 0
    RIGHT_JOIN = 1

    def __init__(self, to_join_table, left_column, right_column, join_type=0):
        self.to_join_table = to_join_table
        self.left_column = left_column
        self.right_column = right_column
        self.join_type = join_type