import csv


def get_csv_header(file_path) -> list:
    with open(file_path, 'r') as read_obj:
        reader = csv.reader(read_obj)
        return next(reader)


def csv_to_list_of_list(file_path, with_header=False) -> list:
    with open(file_path, 'r') as read_obj:
        reader = csv.reader(read_obj)
        if not with_header:
            next(reader)
        return list(reader)
