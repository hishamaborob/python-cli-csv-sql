"""
Sql service may act/or can be seen as an a mini sql server.
It takes a statement, tokenize it, build a plan, and then execute it ans return the result.
It has multiple dependencies (statement tokenizer, statement plan builder, and tables/data/repositories manager).
"""
from data.tables_manager import TablesManager
from entity.result import Result
from helper.sql_statement_tokenizer import SqlStatementTokenizer
from plan.sql_plan_builder import SqlPlanBuilder


class SqlService:
    def __init__(self, sql_statement_tokenizer: SqlStatementTokenizer, sql_planner: SqlPlanBuilder,
                 tables_manager: TablesManager):
        self.__tables_manager = tables_manager
        self.__sql_statement_tokenizer = sql_statement_tokenizer
        self.__sql_planner = sql_planner

    def execute_statement(self, sql_statement: str) -> Result:
        sql_statement_tokens = self.__sql_statement_tokenizer.tokenize_sql_statement(sql_statement)
        if not sql_statement_tokens:
            raise Exception("Invalid statement")
        plan = self.__sql_planner.build(sql_statement_tokens)
        try:
            return plan.execute(self.__tables_manager)
        except Exception as e:
            raise Exception("Could not execute statement. {}".format(str(e)))
