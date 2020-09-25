import os
from unittest import TestCase

from helper import data_builder


class TestDataBuilder(TestCase):
    def test_table_manager_of_csv_files(self):
        data_dir = os.path.dirname(os.path.abspath(__file__)) + "/data"
        files = os.listdir(data_dir)
        csv_files_paths = [data_dir + "/" + filename for filename in files if
                           filename.endswith(".csv") and os.path.isfile(data_dir + "/" + filename)]
        tables_manager = data_builder.table_manager_of_csv_files(csv_files_paths)
        self.assertTrue(tables_manager)
        self.assertTrue(len(tables_manager.get_tables_names()) == 2)
        self.assertTrue("techcrunch_test_data" in tables_manager.get_tables_names())
        self.assertTrue("techcrunch-full" in tables_manager.get_tables_names())
