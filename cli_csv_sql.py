"""
Main Bootstrap and dependencies builder
"""
import argparse
import os
import sys
from helper import data_builder
from helper.sql_statement_tokenizer import SqlStatementTokenizer
from plan.sql_plan_builder import SqlPlanBuilder
from plan.statements_plans_map import main_statements_plans_map
from service.sql_service import SqlService
from util.print_util import print_list_of_lists_as_table

file_extension = ".csv"
my_parser = argparse.ArgumentParser(prog="cli_csv_sql", usage="%(prog)s [options] path",
                                    description="List csv based tables in a folder")

my_parser.add_argument("Path", metavar="path", type=str, help="The path to the folder")

args = my_parser.parse_args()
input_path = args.Path

if not os.path.isdir(input_path):
    print("The path specified does not exist")
    sys.exit()

files = os.listdir(input_path)
csv_files_paths = [input_path + "/" + filename for filename in files if
                   filename.endswith(file_extension) and os.path.isfile(input_path + "/" + filename)]

tables_manager = data_builder.table_manager_of_csv_files(csv_files_paths)
sql_statement_tokenizer = SqlStatementTokenizer()
sql_planner = SqlPlanBuilder(main_statements_plans_map)
sql_service = SqlService(sql_statement_tokenizer, sql_planner, tables_manager)

print("{} Tables:".format(len(tables_manager.get_tables_names())))
print('\n'.join([table_name for table_name in tables_manager.get_tables_names()]))

while True:
    user_input = input("{}=#".format(input_path))
    if not user_input:
        continue
    elif user_input == "q":
        sys.exit()
    else:
        try:
            result = sql_service.execute_statement(user_input)
            print("{} records returned: ".format(result.get_count()))
            list_of_records = result.get_records()
            list_of_records.insert(0, result.get_header())
            print_list_of_lists_as_table(list_of_records)
        except Exception as err:
            print("Execution failed. {}".format(str(err)))
