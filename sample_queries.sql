-- Example 1: Unoptimized Query
SELECT *
FROM large_table
WHERE date >= '2023-01-01' AND date <= '2023-12-31'
ORDER BY date;

-- Optimized Query
SELECT specific_columns
FROM large_table
WHERE date BETWEEN '2023-01-01' AND '2023-12-31'
ORDER BY date
LIMIT 100;  -- Adding a LIMIT to reduce data retrieval

-- Example 2: Using Indexes
SELECT *
FROM large_table
WHERE user_id = 12345;  -- Slow query without an index on 'user_id'

-- Optimized Query with Index
CREATE INDEX idx_user_id ON large_table (user_id);

SELECT specific_columns
FROM large_table
WHERE user_id = 12345;  -- Query now uses the index on 'user_id'

-- Example 3: Partitioned Table Query
SELECT *
FROM large_table
WHERE date = '2023-10-01';

-- Optimized Query with Partitioning
-- Assuming table is partitioned by 'date'
SELECT specific_columns
FROM large_table
WHERE date = '2023-10-01';