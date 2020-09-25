"""
Special implementation of Table Repository that holds CSV data in memory.
Indexes can be added here in the future.
"""


class Table:
    def __init__(self, name: str, columns_positions: dict, data: list):
        self.__name = name
        self.__columns_positions = columns_positions
        self.__data = data

    def get_name(self):
        return self.__name

    def get_columns_positions(self) -> dict:
        return self.__columns_positions

    def get_data(self) -> list:
        return self.__data
