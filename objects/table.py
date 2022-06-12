"""
class Table:
----
This class is a physical representation of a table in an SQL database.
"""
#from objects.bigint import BigInt
import inspect

from objects.decimal import Decimal
from objects.integer import Integer
from objects.smallint import SmallInt
from objects.text import Text


#LIST_OF_TYPES = [BigInt, Decimal, Integer, SmallInt, Text]
from registries.table_registry import TableRegistry


class Table:
    __all = "*"

    def __init__(self, table_registry: TableRegistry):
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


