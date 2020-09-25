"""
Simple Tables plan that holds multiple tables.
Can be the place to support joins in the future.
"""


class TablesPlan:
    def __init__(self, tables_list: list):
        self.__tables = list(filter(lambda v: (v not in {",", "(", ")"}), tables_list))
        if not bool(self.__tables):
            raise Exception("Invalid query. Table name is missing")
        if len(self.__tables) > 1:
            # Currently supporting one table
            raise Exception("Invalid query, or multiple tables query is not supported.")

    def get_tables_name(self):
        return self.__tables.copy()
