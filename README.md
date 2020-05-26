# strangerqueries

strangerqueries is a simple package to run Hive and Impala queries within your python enviroment whilst connecting to a remote repo

from strangerqueries import hive_query, impala_query

Comprises of two methods
hive_query() and impala_query()

Example query

strangerqueries.impala_query(input_sql = "SELECT * FROM ..", db_name ="impala-dc3.example.corp/", output_file_name="output.csv", export_csv =True, sql_file=False)
