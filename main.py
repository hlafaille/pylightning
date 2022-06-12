from builders.select_builder import SelectBuilder
from objects.bigint import BigInt
from objects.join import Join
from objects.table import Table
from objects.text import Text

# define objects
class Employees(Table):
    id = BigInt(primary=True)
    first_name = Text()


class Transactions(Table):
    id = BigInt(primary=True)


# instantiate objects (triggers subclass to handle registering superclass as owner of fields) (by far the worst part of this setup)
employees = Employees()
transactions = Transactions()

# query generator
get_administrators = SelectBuilder(columns=[Employees.id, Employees.first_name, Transactions.id],
                                   joins=[Join(to_join_column=Transactions, left_column=Employees.id, right_column=Transactions.id, join_type=Join.LEFT_JOIN)])

# print query
print(get_administrators)
