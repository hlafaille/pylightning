"""
class SelectBuilder:
----
This class functions as an object for assembling an SQL SELECT statement based on the passed arguments.
SelectBuilder takes a list of columns specified in classes that subclass the Table class, using PostgreSQL datatypes.

SelectBuilder also contains some settings:
lower_case_tables=False --- When True is passed, table names will be automatically lowercase to allow class names to conform with PEP-8
"""
from objects.join import Join


class SelectBuilder:
    def __init__(self, columns: list, lower_case_tables=False):
        # args passed on class instantiation
        self.columns = columns

        # set by join()
        self.joins = []

        # set by group_by()
        self.group_by_column = ""

        # variables that will change
        self.tables_encountered = []

        # Settings
        self.lower_case_tables = lower_case_tables

    # todo replace with the same arguments from the Join object
    # Appends a Join object
    def join(self, join: Join):
        self.joins.append(join)
        return self

    # Sets a group by column
    def group_by(self, group_by):
        self.group_by_column = group_by
        return self

    # Return the SQL command
    def __str__(self):
        base_sql = "SELECT"
        first_table_encountered = ""

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

            # set the first table encountered
            if element == 0:
                if self.lower_case_tables:
                    first_table_encountered = column.table.__class__.__name__.lower()
                else:
                    first_table_encountered = column.table.__class__.__name__

        # add from table (if we've only seen one kind of table, append it...)
        if len(set(self.tables_encountered)) == 1:
            base_sql += "FROM {0}".format(first_table_encountered)
        else:
            # looks like there was more than one table specified, attempting to get 'JOIN'
            base_sql += "FROM {0}".format(first_table_encountered)

            # lets figure out how we're gonna get this join done :/
            for element, join in enumerate(self.joins):
                if self.lower_case_tables:
                    to_join_table_name = join.to_join_table.__name__.lower()
                    left_table_name = join.left_column.table.__class__.__name__.lower()
                    right_table_name = join.right_column.table.__class__.__name__.lower()
                else:
                    to_join_table_name = join.to_join_table.__name__
                    left_table_name = join.left_column.table.__class__.__name__
                    right_table_name = join.right_column.table.__class__.__name__

                # determine if this is a left or right join
                if join.join_type == join.LEFT_JOIN:
                    base_sql += " LEFT JOIN {0}".format(to_join_table_name)
                elif join.join_type == join.RIGHT_JOIN:
                    base_sql += " RIGHT JOIN {0}".format(to_join_table_name)

                base_sql += " ON {0}.{1}={2}.{3}".format(left_table_name, join.left_column.name, right_table_name, join.right_column.name)

        # append ';'
        base_sql += ";"
        return base_sql
