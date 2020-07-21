# strangerqueries

strangerqueries is a simple package to run Hive and Impala queries within a Cloudera enviroment whilst connecting to a remote database.

Comprises of two methods
hive_query() and impala_query()

Example query

from strangerqueries import queries

test = queries.beeline()

test.impala_query(input_sql = "SELECT * FROM ..", db_name ="impala-dc3.example.corp/", output_file_name="output.csv", export_csv =True, sql_file=False)
