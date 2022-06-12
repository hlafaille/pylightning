class IncorrectColumnTypeException(Exception):
    def __init__(self, table, column):
        super().__init__("Incorrect column type in table '{0}' with type '{1}'. Please read the documentation for supported PostgreSQL datatypes.".format(table.name, type(column).__name__))