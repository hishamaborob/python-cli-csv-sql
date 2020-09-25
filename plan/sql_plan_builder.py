"""
A statement plan builder that takes the tokenized statement and map it to the concrete plan (Select, Update, ..)
"""
from plan.main.sql_plan import SqlPlan


class SqlPlanBuilder:
    def __init__(self, __statements_plans_map: dict):
        self.__statements_plans_map = __statements_plans_map

    def build(self, sql_statement_tokens: list) -> SqlPlan:
        main_statement = str(sql_statement_tokens[0]).lower()
        if main_statement not in self.__statements_plans_map:
            raise Exception(
                "Statement is not supported. Supported statements: {}".format(self.__statements_plans_map.keys()))
        if not sql_statement_tokens[-1] == ";":
            raise Exception("Invalid statement. Missing ( ; )")
        if not main_statement in self.__statements_plans_map:
            raise Exception("Statement {} not supported.".format(main_statement))
        return self.__statements_plans_map[main_statement](sql_statement_tokens)
