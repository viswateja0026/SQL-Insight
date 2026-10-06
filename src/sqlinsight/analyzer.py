from sqlglot import exp


def analyze_query(ast):
    tables = [
        table.name
        for table in ast.find_all(exp.Table)
    ]

    columns = [
        column.name
        for column in ast.find_all(exp.Column)
    ]

    return {
        "tables": tables,
        "columns": columns
    }