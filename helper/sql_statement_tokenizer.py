"""
Statement tokenizer that splits sql statement into an easy to navigate through list
"""
import re
import shlex


class SqlStatementTokenizer:
    def tokenize_sql_statement(self, sql_statement: str) -> list:
        cleaned_sql_statement = self.clean_sql_statement(sql_statement)
        lexer = shlex.split(cleaned_sql_statement)
        return list(str(token) for token in lexer)

    # Not the ideal implementation of cleaner function and it's definitely slow :)
    def clean_sql_statement(self, sql_statement: str):
        sql_statement = sql_statement.strip()
        sql_statement = sql_statement.replace("’", "'").replace("‘", "'")
        sql_statement = sql_statement.replace("=", " = ").replace("!=", " != ")
        sql_statement = sql_statement.replace(";", " ; ").replace(",", " , ")
        return re.sub("\s\s+", " ", sql_statement)
