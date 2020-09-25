"""
Mapping of main statements (Select, update, ..) to the plan.
"""
from plan.main.sql_select_plan import SqlSelectPlan


def create_select_plan(sql_statement_tokens: list):
    return SqlSelectPlan(sql_statement_tokens)


main_statements_plans_map = {
    "select": create_select_plan
}
