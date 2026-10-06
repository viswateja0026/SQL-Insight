import sqlglot
def parse_sql(query: str):
    return sqlglot.parse_one(query)