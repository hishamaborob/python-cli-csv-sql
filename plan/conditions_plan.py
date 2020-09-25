"""
Conditions plan that supports multiple conditions and operators.
It has two algorithms, one for validating the tokenized conditions plan
and the other works on the list of records and tokens recursively to filter records.
Maybe this class/file can be broken into more smaller reusable pieces.
"""
import plan.parameters as params
import re


def is_valid(conditions_list):
    counter = 0
    for condition in conditions_list:
        if counter in [0, 2] and (condition in params.conditions or condition in params.condition_operators):
            return False
        if counter == 1 and condition not in params.condition_operators:
            return False
        if counter == 3:
            if str(condition).lower() not in params.conditions:
                return False
            else:
                counter = 0;
                continue
        counter += 1
    return counter == 3


# Recursive function for applying conditions
def is_record_included(record: list, conditions: list, columns_positions: dict, condition_pointer: int):
    is_included = False
    condition = conditions[condition_pointer]
    if condition not in params.conditions or condition not in params.condition_operators:
        column_position = columns_positions.get(condition)
        condition_operator = conditions[condition_pointer + 1]
        condition_value = clean_value(conditions[condition_pointer + 2])
        is_included = compare_values(record, condition_operator, column_position, condition_value)
        condition_pointer += 3
    if condition_pointer < len(conditions):
        condition = str(conditions[condition_pointer]).lower()
        condition_pointer += 1
        if condition == "and":
            return is_included and is_record_included(record, conditions, columns_positions, condition_pointer)
        elif condition == "or":
            return is_included or is_record_included(record, conditions, columns_positions, condition_pointer)
    return is_included


def compare_values(record, condition_operator, column_position, condition_value):
    is_included = False
    if condition_operator == "=":
        is_included = record[column_position] == condition_value
    elif condition_operator == "!=":
        is_included = record[column_position] != condition_value
    return is_included


def clean_value(value: str):
    return re.sub('\W+', '', value)


class ConditionsPlan:
    def __init__(self, conditions_list: list):
        self.__conditions = conditions_list.copy()
        if not bool(self.__conditions) or not is_valid(self.__conditions):
            raise Exception("Invalid query, Wrong conditions, or some operators are not supported")

    def apply(self, list_of_records: list, columns_positions: dict) -> list:
        return list(filter(lambda record: (is_record_included(record, self.__conditions, columns_positions, 0)),
                           list_of_records))
