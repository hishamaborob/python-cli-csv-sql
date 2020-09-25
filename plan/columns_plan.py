"""
Columns plan that supports simple count, select *, and selected columns.
It gets applied on list of records.
"""
import plan.parameters as param
from entity.result import Result


def is_valid(select_all_columns, select_count, columns):
    if select_all_columns or select_count:
        return True
    elif bool(columns):
        return True
    else:
        return False


class ColumnsPlan:
    def __init__(self, columns_list: list):
        self.__select_all_columns = False
        self.__select_count = False
        self.__columns = set()
        for column in columns_list:
            if column == param.all_columns:
                self.__select_all_columns = True
            if str(column).lower() in param.count_function:
                # Currently limited functionality
                self.__select_count = True
            elif column not in {",", "(", ")"}:
                self.__columns.add(column)
        if not is_valid(self.__select_all_columns, self.__select_count, self.__columns):
            raise Exception("Invalid query. columns name is missing")

    def apply(self, list_of_records: list, columns_positions: dict) -> Result:
        # Currently it's based on priority
        if self.__select_count:
            return Result(["count"], [[len(list_of_records)]])
        elif self.__select_all_columns:
            return Result(sorted(columns_positions, key=columns_positions.get), list_of_records)
        else:
            selected_columns_positions = {k: v for (k, v) in columns_positions.items() if k in self.__columns}
            list_of_records = list(
                map(lambda record: [record[i] for i in selected_columns_positions.values()], list_of_records))
            return Result(sorted(selected_columns_positions, key=selected_columns_positions.get), list_of_records)
