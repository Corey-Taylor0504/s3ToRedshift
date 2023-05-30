
# Delete existing table named "iris"
sql_query = """DROP TABLE IF EXISTS iris"""
execute_sql(sql_query, conn_string)

# Create a new table named "iris"
sql_query = """CREATE TABLE IF NOT EXISTS iris_3
               (
               sepal_length NUMERIC,
               sepal_width NUMERIC,
               petal_length NUMERIC,
               petal_width NUMERIC,
               species VARCHAR
               )
            """
execute_sql(sql_query, conn_string)

# Define S3 source file path
file_path = "s3://data-to-migrate/iris_dataset.csv"

# Copy data
sql_query = """
  COPY iris_3
  FROM '{}'
  IAM_ROLE '{}' 
  csv
  IGNOREHEADER 1
  ;
""".format(file_path, role_arn)
execute_sql(sql_query, conn_string)