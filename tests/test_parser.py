from sqlinsight.parser import parse_sql


def test_parse_sql():
    query = "SELECT name FROM users WHERE age > 18"

    result = parse_sql(query)

    assert result is not None

   
from sqlinsight.analyzer import analyze_query


def test_analyze_query():
    query = "SELECT name, age FROM users WHERE age > 18"

    ast = parse_sql(query)
    result = analyze_query(ast)

    assert result["tables"] == ["users"]
    assert "name" in result["columns"]
    assert "age" in result["columns"]