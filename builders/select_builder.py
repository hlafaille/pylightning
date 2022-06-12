"""
class SelectBuilder:
----
This class functions as an object for assembling an SQL SELECT statement based on the passed arguments.
SelectBuilder takes a list of columns specified in classes that subclass the Table class, using PostgreSQL datatypes.

SelectBuilder also contains some settings:
lower_case_tables=False --- When True is passed, table names will be automatically lowercase to allow class names to conform with PEP-8
"""


class SelectBuilder:
    def __init__(self, columns: list, lower_case_tables=False, joins=None):
        # args passed on class instantiation
        self.columns = columns
        self.joins = joins

        # variables that will change
        self.tables_encountered = []

        # Settings
        self.lower_case_tables = lower_case_tables

    # Return the SQL command
    def __str__(self):
        base_sql = "SELECT"

        # add columns
        for element, column in enumerate(self.columns):
            if self.lower_case_tables:
                table_name = column.table.__class__.__name__.lower()
            else:
                table_name = column.table.__class__.__name__

            # keep track of all tables we've seen, this will allow us to determine our 'FROM' table name
            self.tables_encountered.append(table_name)

            # if we're at the first and only element
            if element == 0 and len(self.columns) == 1:
                base_sql += " {0}.{1} ".format(table_name, column.name)

            # if we're not at the last element
            elif not element == len(self.columns) - 1:
                base_sql += " {0}.{1}, ".format(table_name, column.name)

            # if we're at the last element, and we have more than one
            elif element == len(self.columns) - 1:
                base_sql += "{0}.{1} ".format(table_name, column.name)

        # add from table (if we've only seen one kind of table, append it...)
        if len(set(self.tables_encountered)) == 1:
            base_sql += "FROM {0}".format(list(set(self.tables_encountered))[0])
        else:
            # looks like there was more than one table specified, attempting to get 'JOIN'
            base_sql += "FROM {0}".format(list(set(self.tables_encountered))[0])

            # lets figure out how we're gonna get this join done :/
            for element, join in enumerate(self.joins):
                if self.lower_case_tables:
                    left_table_name = join.left_column.table.__class__.__name__.lower()
                    right_table_name = join.right_column.table.__class__.__name__.lower()
                else:
                    left_table_name = join.left_column.table.__class__.__name__
                    right_table_name = join.right_column.table.__class__.__name__

                # determine if this is a left or right join
                if join.join_type == join.LEFT_JOIN:
                    base_sql += " LEFT JOIN"
                elif join.join_type == join.RIGHT_JOIN:
                    base_sql += " RIGHT JOIN"

                base_sql += " WHERE {0}.{1}={2}.{3}".format(left_table_name, join.left_column.name, right_table_name, join.right_column.name)
        return base_sql
