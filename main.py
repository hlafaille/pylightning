from builders.select_builder import SelectBuilder
from objects.bigint import BigInt
from objects.table import Table
from objects.text import Text

class Employees(Table):
    id = BigInt(primary=True)
    first_name = Text()


class Transactions(Table):
    id = BigInt(primary=True)

employees = Employees()
transactions = Transactions()

get_administrators = SelectBuilder(columns=[Employees.id, Employees.first_name, Transactions.id])

print(get_administrators)
