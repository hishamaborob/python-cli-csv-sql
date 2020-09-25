"""
Abstract class for main statements plans to implement
"""
from data.tables_manager import TablesManager
from entity.result import Result


class SqlPlan:
    def execute(self, tables_manager: TablesManager) -> Result:
        pass
