from unittest import TestCase

from helper.sql_statement_tokenizer import SqlStatementTokenizer


class TestSqlStatementTokenizer(TestCase):
    def test_sql_statement_tokenizer(self):
        sql_statement_tokenizer = SqlStatementTokenizer()
        statement = "SELECT  first_name, last_name    FROM drivers WHERE country = ‘USA';"
        tokens = sql_statement_tokenizer.tokenize_sql_statement(statement)
        self.assertEqual(
            ["SELECT", "first_name", ",", "last_name", "FROM", "drivers", "WHERE", "country", "=", "USA", ";"], tokens)
