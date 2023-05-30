def execute_sql(
  sql_query,
  conn_string,
  print_results = False
  ):
  """Execute a SQL query on the datavbase associated with a connection string

  Parametrs:
  - sql_query : str
    SQL queyr to execute
    -conn_string : str
    connection string ot the format 'postgresql://MasterUsername:MasterUSerPAsswors@ClusterEndpoint:DatabasePort, DatabaseName'
  """

  # Connect to the datavase
  conn = psycopg2.connect(conn_string)

  # Define cursor()
  cur = conn.cursor()

  # Execute query
  cur.execute(sql_query)
  conn.commit()
  if print_results:
    print(cur.fetchall())
  
  # Close cursor
  cur.close()

  # Close connection
  conn.close()