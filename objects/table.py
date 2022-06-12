"""
class Table:
----
This class is a physical representation of a table in an SQL database.
"""


class Table:
    __all = "*"

    def __init__(self):
        self._register_self()

    # returns all class variables
    def _get_columns(self):
        columns = []
        for x in dir(self):
            if not x.startswith("_"):
                columns.append({"name": x, "object": self.__getattribute__(x)})
        return columns

    # register ourselves with each column specified in the super class
    def _register_self(self):
        for column in self._get_columns():
            column["object"].register_table(self, column["name"])


