import psycopg2

# Define connection string
%load_ext sql
conn_string = "postgresql://{}:{}@{}/{}".format(
    username,
    password,
    cluster_endpoint,
    port,
    database_name
)

# Test connection
%sql $conn_string