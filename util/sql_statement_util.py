"""
Util to help navigate through statement tokens
"""


def find_new_pointer_position(current_pointer, tokens_list: list, end_statements):
    end_pointer = 0
    while tokens_list and str(tokens_list[current_pointer + end_pointer]).lower() not in end_statements:
        end_pointer += 1
    return current_pointer + end_pointer
