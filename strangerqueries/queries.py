import numpy as np
import pandas as pd
import subprocess
import os
from time import time

class beeline():

    """
    This class enables users to easily run Hive and Impala queries in python to a database of there choice
    """

    def __init__(self, export_csv=True, sql_file=True):
        self.export_csv = export_csv
        self.sql_file = sql_file
        """
        Parameters:
        ----
        export_csv: bool, (default=true)
        to export query into csv, can be true or false
        Note: if set to true, ensure that output_file_name is set

        sql_file: bool, (default = True)
            If you wish to use a local sql_file set input_sql to path
            If you want to run the code straight from input_sql set to False, e.g. input_sql = "SELECT * FROM..."

        """




    def hive_query(self, input_sql, db_name, output_file_name=None, export_csv=True, sql_file=True):
        """
        This is the method for running hive queries

        Parameters:
        ---------
        input_sql: str, (default=None)
            Used to either input the dql file e.g. test.sql_file
            or to import the sql_code directly e.g. "SELECT * FROM ..."

        db_name: str, {default= None}:
            specify the database you wish to peform queries in e.g. 'impala-dc3.example.corp'


        output_file_name: str, optional (default=None)
            Used to output the name of the csv, from the query.
            E.g. output_file_name = test.export_csv
            Note1: ensure you put .csv at the end of the file name
            Note2: only required if export_csv = True

        export_csv: bool, (default=true)
            to export query into csv, can be true or false
            Note: if set to true, ensure that output_file_name is set

        sql_file: bool, (default = True)
            If you wish to use a local sql_file set input_sql to path
            If you want to run the code straight from input_sql set to False, e.g. input_sql = "SELECT * FROM..."

        """

        self.input_sql = input_sql
        output_format = "csv2"
        if sql_file:
            command = f"beeline -u {db_name} --output_format={output_format} --verbose=false --fastConnect=true --silent=false -f {input_sql}"
        else:
            command = f"beeline -u {db_name} --output_format={output_format} --verbose=false --fastConnect=true -e {input_sql} --silent=false"
        if export_csv:
            with open(output_file_name, "wb") as outfile:
                command_split = command.split()

                if not(sql_file):
                    command_split.append(input_sql)

                subprocess.call(command_split, stdout=outfile)

            if sql_file:
                output_df = pd.read_csv(output_file_name, error_bad_lines=False, encoding='utf-8', header=1)
            else:
                output_df = pd.read_csv(output_file_name)
            output_df.rename(columns=lambda x: x.split('.')[1].replace(' ','_') if '.' in x else x, inplace= True)
            output_df.to_csv(output_file_name, index=False)

        else:
            command_split = command.split()
            if not(sql_file):
                command_split.append(input_sql)
            subprocess.call(command_split)

    def impala_query(self, input_sql, db_name, output_file_name=None, export_csv=True, sql_file=True):
        """
        This is the method for running hive queries

        Parameters:
        ---------
        input_sql: str, (default=None)
            Used to either input the dql file e.g. test.sql_file
            or to import the sql_code directly e.g. "SELECT * FROM ..."

        db_name: str, {default= None}:
            specify the database you wish to peform queries in e.g. 'impala-dc3.example.corp'

        output_file_name: str, optional (default=None)
            Used to output the name of the csv, from the query.
            E.g. output_file_name = test.export_csv
            Note1: ensure you put .csv at the end of the file name
            Note2: only required if export_csv = True

        export_csv: bool, (default=true)
            to export query into csv, can be true or false
            Note: if set to true, ensure that output_file_name is set

        sql_file: bool, (default = True)
            If you wish to use a local sql_file set input_sql to path
            If you want to run the code straight from input_sql set to False, e.g. input_sql = "SELECT * FROM..."

        """
        self.input_sql = input_sql
        output_format = 'csv2'
        if sql_file:
            command = f"impala-shell -B -k -c -i {db_name} --output_delimiter=, --print_header -f {input_sql} -o"
        else:
            command = f"impala-shell -B -k -c -i {db_name} --output_delimiter=, -o {output_file_name} --print_header -q"
        command_split = command.split()
        if not(sql_file):
            command_split.append(input_sql)
        if sql_file:
            command_split.append(output_file_name)
        subprocess.call(command_split)
