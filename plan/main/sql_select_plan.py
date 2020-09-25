"""
Sql Select Plan accept a tokenized statement and construct a plan to execute the query.
It has multiple dependencies (columns plan, conditions plan, tables plan)
which get also constructed and executed in a chain.
"""
from data.tables_manager import TablesManager
from entity.result import Result, empty_result
from util.sql_statement_util import find_new_pointer_position
from plan.columns_plan import ColumnsPlan
from plan.conditions_plan import ConditionsPlan
from plan.main.sql_plan import SqlPlan
from plan.tables_plan import TablesPlan
import plan.parameters as params

select_statement_plan_structure = {
    params.select_statement: {
        "end": [params.from_statement]
    },
    params.from_statement: {
        "end": [params.where_statement, params.statement_close]
    },
    params.where_statement: {
        "end": [params.statement_close]
    },
}


class SqlSelectPlan(SqlPlan):

    # Can be refactored and made a bit shorter
    def __init__(self, sql_statement_tokens: list):
        self.__conditions_plan = None
        tokens = sql_statement_tokens.copy()
        pointer = 0
        while pointer < len(tokens):
            current_token = str(tokens[pointer]).lower()
            pointer += 1
            if current_token in select_statement_plan_structure:
                try:
                    new_pointer = find_new_pointer_position(
                        pointer, tokens, select_statement_plan_structure.get(current_token).get("end"))
                except IndexError:
                    raise Exception("Invalid syntax.")
                plan_tokens = tokens[pointer:new_pointer]
                if current_token == params.select_statement:
                    self.__columns_plan = ColumnsPlan(plan_tokens)
                elif current_token == params.from_statement:
                    self.__tables_plan = TablesPlan(plan_tokens)
                elif current_token == params.where_statement:
                    self.__conditions_plan = ConditionsPlan(plan_tokens)
                pointer = new_pointer
        if not self.__columns_plan or not self.__tables_plan:
            raise Exception("Invalid syntax.")

    def execute(self, tables_manager: TablesManager) -> Result:
        list_of_records = list()
        # Currently supporting one table
        table_name = self.__tables_plan.get_tables_name()[0]
        table = tables_manager.get_table(table_name)
        columns_positions = table.get_columns_positions()
        if self.__conditions_plan:
            list_of_records = self.__conditions_plan.apply(table.get_data(), columns_positions)
        else:
            list_of_records = table.get_data()
        if bool(list_of_records):
            return self.__columns_plan.apply(list_of_records, columns_positions)
        return empty_result()
