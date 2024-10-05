from query_optimizer import SQLQueryOptimizer
from benchmarks import compare_queries

# Initialize connection to your database (use your own connection string)
connection_string = "postgresql://user:password@localhost:5432/mydatabase"
optimizer = SQLQueryOptimizer(connection_string)

# Sample queries
original_query = """
SELECT *
FROM large_table
WHERE date >= '2023-01-01' AND date <= '2023-12-31'
ORDER BY date;
"""

optimized_query = optimizer.optimize_query(original_query)

# Run benchmarks
compare_queries(optimizer, original_query, optimized_query)

# Example: Creating index and partitioning for optimization
optimizer.create_index('large_table', 'user_id')
optimizer.partition_table('large_table', 'date')

# Analyzing query execution with EXPLAIN
explain_plan = optimizer.explain_query(optimized_query)
print(explain_plan)