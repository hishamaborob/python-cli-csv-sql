def print_list_of_lists_as_table(records_list: list):
    length_list = [len(str(element)) for row in records_list for element in row]
    column_width = max(length_list)
    for row in records_list:
        row = "".join(str(element).ljust(column_width + 2) for element in row)
        print(row)
