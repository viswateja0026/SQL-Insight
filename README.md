# SQL Insight

SQL Insight is a Python-based developer tool for analyzing SQL queries and providing actionable insights about query structure, quality, performance, and potential issues.

The project is being developed as a reusable Python package with support for CLI, REST API, and database-level analysis.

---

## Problem

Developers often manually inspect SQL queries to identify potential issues such as:

- Unnecessary columns
- `SELECT *`
- Missing filters
- Inefficient joins
- Complex queries
- Potential performance bottlenecks

SQL Insight aims to automate this initial analysis and provide clear recommendations.

---

## Key Features

### SQL Query Analysis
- SQL parsing using SQLGlot
- Abstract Syntax Tree (AST) analysis
- Table and column extraction
- JOIN detection
- WHERE, GROUP BY and ORDER BY analysis
- Aggregation detection
- Subquery and CTE analysis

### SQL Quality Analysis
- Detect potentially problematic SQL patterns
- Rule-based SQL analysis
- Query quality checks
- Maintainability checks

### Performance Analysis
- SQL performance checks
- Database execution-plan analysis
- `EXPLAIN` analysis
- Potential index recommendations
- Query benchmarking

### Developer Tools
- Query comparison
- Query history
- Health score
- JSON and HTML reports
- Command-line interface
- REST API
- CI/CD integration

---

## Architecture

```text
SQL Query
    |
    v
SQL Parser
   (SQLGlot)
    |
    v
AST
    |
    v
Query Analyzer
    |
    v
Rule Engine
    |
    v
Performance / Security / Quality Analysis
    |
    v
Insights & Recommendations
    |
    v
CLI / REST API / Dashboard