"""
Full integration test. (not 100% test coverage :))
"""
import os
from unittest import TestCase

from helper import data_builder
from helper.sql_statement_tokenizer import SqlStatementTokenizer
from plan.sql_plan_builder import SqlPlanBuilder
from plan.statements_plans_map import main_statements_plans_map
from service.sql_service import SqlService


class CliToolIntegrationTest(TestCase):
    def test_execute_sql_statement(self):
        data_dir = os.path.dirname(os.path.abspath(__file__)) + "/data"
        files = os.listdir(data_dir)
        csv_files_paths = [data_dir + "/" + filename for filename in files if
                           filename.endswith(".csv") and os.path.isfile(data_dir + "/" + filename)]
        tables_manager = data_builder.table_manager_of_csv_files(csv_files_paths)
        sql_statement_tokenizer = SqlStatementTokenizer()
        sql_planner = SqlPlanBuilder(main_statements_plans_map)
        sql_service = SqlService(sql_statement_tokenizer, sql_planner, tables_manager)

        result = sql_service.execute_statement("SELECT company,city FROM techcrunch_test_data WHERE company='Digg';")
        self.assertTrue(result and result.get_count() == 2)
        self.assertEqual(["company", "city"], result.get_header())
        self.assertEqual(['Digg', 'San Francisco'], result.get_records()[0])
        self.assertEqual(['Digg', 'San Francisco'], result.get_records()[1])

        result = sql_service.execute_statement("SELECT * FROM techcrunch_test_data WHERE company='Facebook';")
        self.assertTrue(result and result.get_count() == 1)
        self.assertEqual(['permalink', 'company', 'numEmps', 'category', 'city', 'state', 'fundedDate', 'raisedAmt',
                          'raisedCurrency', 'round'], result.get_header())
        self.assertEqual(
            ['facebook', 'Facebook', '450', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel'],
            result.get_records()[0])

        result = sql_service.execute_statement(
            "SELECT count(*) FROM techcrunch_test_data WHERE company='Digg' OR category='software';")
        self.assertTrue(result and result.get_count() == 1)
        self.assertEqual([3],result.get_records()[0])

        result = sql_service.execute_statement(
            "select company,numEmps from techcrunch_test_data where numEmps=4;")
        self.assertTrue(result and result.get_count() == 1)
        self.assertEqual(['gAuto', '4'],result.get_records()[0])
