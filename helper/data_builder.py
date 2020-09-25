"""
Helper for loading data from CSV files and creating Tables manager
"""
from util import csv_reader
from os.path import splitext, basename
from data.tables_manager import TablesManager
from data.table import Table


def table_manager_of_csv_files(csv_files_paths: list) -> TablesManager:
    tables_manager = TablesManager()
    for file_path in csv_files_paths:
        header = csv_reader.get_csv_header(file_path)
        data = csv_reader.csv_to_list_of_list(file_path)
        if header and data:
            try:
                tables_manager.add_table(
                    Table(get_file_name_from_path(file_path), header_to_columns_positions(header), data))
            except Exception as e:
                print("Error loading table {}: {}".format(file_path, str(e)))
    return tables_manager


def header_to_columns_positions(header: list) -> dict:
    return dict(map(lambda v: (v[1], v[0]), enumerate(header)))


def get_file_name_from_path(file_path: str):
    return splitext(basename(file_path))[0]
