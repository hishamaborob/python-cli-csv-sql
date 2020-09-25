"""
Special implementation of a data manager that holds pointer and information
about available tables
"""
from data.table import Table


class TablesManager:
    def __init__(self):
        self.__tables = {}

    def add_table(self, table: Table):
        if table is None:
            raise Exception("Table cannot be empty")
        if not table.get_name():
            raise Exception("Table name cannot be empty")

        self.__tables[table.get_name()] = table

    def is_table_exist(self, table_name):
        return table_name in self.__tables

    def get_table(self, table_name) -> Table:
        if table_name not in self.__tables:
            raise Exception("Table {} does not exist.".format(table_name))
        return self.__tables.get(table_name)

    def get_tables_names(self) -> list:
        return list(self.__tables.keys())
