from unittest import TestCase

from data.table import Table
from data.tables_manager import TablesManager


class TestTablesManager(TestCase):
    def test_table_manager(self):
        tables_manager = TablesManager()
        table = Table("test", {"a": 0, "b": 1}, [["aa", "bb"]])
        tables_manager.add_table(table)
        table_test = tables_manager.get_table("test")
        self.assertTrue(table_test)
        self.assertTrue(tables_manager.is_table_exist("test"))
        self.assertEqual(tables_manager.get_tables_names(), ["test"])
