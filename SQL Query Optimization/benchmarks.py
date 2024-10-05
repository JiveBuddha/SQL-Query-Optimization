import time
from query_optimizer import SQLQueryOptimizer

def benchmark_query(optimizer, query):
    """
    Benchmark the execution time of a SQL query.

    :param optimizer: SQLQueryOptimizer - An instance of the SQLQueryOptimizer class.
    :param query: str - The SQL query to benchmark.
    :return: float - Execution time in seconds.
    """
    start_time = time.time()
    optimizer.execute_query(query)
    end_time = time.time()

    execution_time = end_time - start_time
    return execution_time

def compare_queries(optimizer, original_query, optimized_query):
    """
    Compare the execution times of an original query and an optimized query.

    :param optimizer: SQLQueryOptimizer - An instance of the SQLQueryOptimizer class.
    :param original_query: str - The original SQL query.
    :param optimized_query: str - The optimized SQL query.
    """
    original_time = benchmark_query(optimizer, original_query)
    optimized_time = benchmark_query(optimizer, optimized_query)

    print(f"Original query execution time: {original_time:.4f} seconds")
    print(f"Optimized query execution time: {optimized_time:.4f} seconds")