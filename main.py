from builders.select_builder import SelectBuilder
from objects.bigint import BigInt
from objects.table import Table
from objects.text import Text
from registries.table_registry import TableRegistry


class Employees(Table):
    id = BigInt(primary=True)
    first_name = Text()


class Transactions(Table):
    id = BigInt(primary=True)


table_registry = TableRegistry()

employees = Employees(table_registry=table_registry)
transactions = Transactions(table_registry=table_registry)

get_administrators = SelectBuilder(columns=[Employees.id, Employees.first_name, Transactions.id])

print(get_administrators)
