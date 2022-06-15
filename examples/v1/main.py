"""
In this example, we will outline the basic functions of pylightning.
"""
from builders.select_builder import SelectBuilder
from objects.bigint import BigInt
from objects.float import Float
from objects.join import Join
from objects.table import Table
from objects.text import Text


# Create a class with the subclass of Table, serves as a representation of a database table.
class Employees(Table):
    # Each column is also represented by an object stored in this class (some can even take arguments!)
    id = BigInt(primary=True)
    first_name = Text(length=25)
    last_name = Text(length=25)
    email = Text()
    password_hash = Text()


class Transactions(Table):
    id = BigInt(primary=True)
    employee = BigInt()
    total = Float(precision=2)


"""
In the above schema structure we have defined an Employees & Transactions table. We will perform a JOIN example.
----
pylightning requires you to create instances of your defined tables, which is a small downside compared to SQLAlchemy.
"""

employees = Employees()
transactions = Transactions()

"""
Now simply define in a builder the columns you want, and any settings the builder may support.
Warning: pylightning runs close to ZERO checks when generating your SQL to verify if it is correct.
This may be changed in the future to maybe have a development mode. For example, builders wont iterate
over your provided columns to determine if their joins are valid, as this wastes valuable interpreter
power. We leave this up to the database to raise an exception.
"""

get_transactions = SelectBuilder(
    columns=[transactions.id, transactions.total, Employees.first_name, Employees.last_name],
    lower_case_tables=True).\
    join(Join(to_join_table=Employees, left_column=transactions.employee, right_column=employees.id)).\
    group_by(transactions.id)

"""
The __str__ of all builders will always return the valid SQL statement based on your input.
"""

print(get_transactions)


