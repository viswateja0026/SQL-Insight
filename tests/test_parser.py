from sqlinsight.parser import parse_sql
from sqlinsight.analyzer import analyze_query, analyze_query_structure


def test_parse_sql():
    query = "SELECT name FROM users WHERE age > 18"

    result = parse_sql(query)

    assert result is not None


def test_analyze_query():
    query = "SELECT name, age FROM users WHERE age > 18"

    ast = parse_sql(query)
    result = analyze_query(ast)

    assert result["tables"] == ["users"]
    assert "name" in result["columns"]
    assert "age" in result["columns"]


def test_analyze_query_clauses():
    query = """
        SELECT department, COUNT(*)
        FROM employees
        WHERE salary > 30000
        GROUP BY department
        ORDER BY department
    """

    ast = parse_sql(query)
    result = analyze_query(ast)

    assert result["has_where"] is True
    assert result["has_group_by"] is True
    assert result["has_order_by"] is True
    assert result["has_join"] is False
    assert "COUNT" in result["aggregation_functions"]


def test_analyze_query_structure():
    query = """
        SELECT DISTINCT name
        FROM employees
        LIMIT 10
    """

    ast = parse_sql(query)
    result = analyze_query_structure(ast)

    assert result["query_type"] == "SELECT"
    assert result["has_subquery"] is False
    assert result["has_distinct"] is True
    assert result["has_limit"] is True