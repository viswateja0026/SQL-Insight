import ast

from sqlglot import exp


def analyze_query_structure(ast):
    tables = sorted({
        table.name
        for table in ast.find_all(exp.Table)
    })

    columns = sorted({
        column.name
        for column in ast.find_all(exp.Column)
    })
    has_where = ast.find(exp.Where) is not None
    has_group_by = ast.find(exp.Group) is not None
    has_order_by = ast.find(exp.Order) is not None
    has_join = ast.find(exp.Join) is not None

    
    aggregation_functions = sorted({
        node.sql_name()
        for node in ast.find_all(exp.AggFunc)
    })

    return {
        "tables": tables,
        "columns": columns,
        "has_where": has_where,
        "has_group_by": has_group_by,
        "has_order_by": has_order_by,
        "has_join": has_join,
        "aggregation_functions": aggregation_functions
    }