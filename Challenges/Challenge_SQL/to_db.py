# https://archive.ics.uci.edu/ml/datasets/Carbon+Nanotubes
# Dataset download and description.

import csv
import logging
import mysql.connector as connection
from tqdm.autonotebook import tqdm

logging.basicConfig(filename='logtest_mysql.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    )


class DbOperations:
    def __init__(self, host,port, user, password, db_name=None ):
        try:
            self.dbname = db_name
            if db_name:
                self.dbConnection = connection.connect(
                    host=host, port = port, user=user, password=password, database=db_name)
            else:
                self.dbConnection = connection.connect(
                    host=host, port=port, user=user, password = password)

            if self.dbConnection.is_connected():
                logging.info("Connection Successful")
            else:
                logging.warning("Not connected to DB")
        except Exception as e:
            logging.exception(e)
            logging.error("Issue in establishing the connection. ")

    def clean_query(self, query):
        """perform the cleaning of query to avoid SQL injection attacks. """
        return query

    def execute_query(self, query, commit=False, log_resp=True):
        query = self.clean_query(query)
        if self.check_connection():
            logging.info(query)
            cursor = self.dbConnection.cursor()
            cursor.execute(query)
            logging.info("Query Executed. ")
            if commit:
                self.dbConnection.commit()
            resp = cursor.fetchall()
            if log_resp:
                logging.info(resp)
            cursor.close()
            return resp
        else:
            logging.warning("Check DB connection. ")
            return None

    def check_connection(self):
        """ This function checks whether the connection is exists or lost. """
        return self.dbConnection.is_connected()

    def is_db_exists(self, db_name):
        """ This function checks if the database exists. """
        query = "SHOW DATABASES;"
        db_response = self.execute_query(query)
        logging.info(db_response)
        return (db_name,) in db_response

    def create_db(self,db_name):
        """ This function is to create the Database. """
        if self.is_db_exists(db_name):
            logging.info(f"Database {db_name} already exists. ")
            return {"status":"exists"}
        else:
            create_db_query = f"Create Database {db_name};"
            db_response = self.execute_query(create_db_query)

            if self.is_db_exists(db_name):
                # self.dbname = db_name
                logging.info("Database created successfully. ")
                return {"status":"created"}
            else:
                logging.warning(f"Issue in creating the database. {db_name}")
                return {"status":None}

    def select_db(self, db_name):
        """ This function is to select the database. """
        if self.is_db_exists(db_name):
            self.dbname = db_name
        else:
            logging.warning(f"{db_name} Database is not present. ")

    # def is_table_exists(self, table_name, database_name=None):
    #     if database_name:
    #         self.select_db(database_name)
    #
    #     query = f"show tables; "
    #     db_response = self.execute_query(query)
    #     logging.info(db_response)
    #     if (table_name, ) in db_response:
    #         logging.info(f"Table {table_name} exists. ")
    #         return True
    #     else:
    #         logging.warning(f"Table {table_name} does not exists. ")

    def create_table(self, table_name, dct_info, database_name=None):
        """ This function is to create the table. """
        if database_name:
            self.select_db(database_name)
            if self.dbname is None:

                logging.warning("Cannot proceed further. ")
        table_columns = ""
        for col_dtype, col_names in dct_info.items():
            for col_name in col_names:
                table_columns += "`" + col_name + "` " + col_dtype + " , "
                # table_columns += "[" + col_name + "] " + col_dtype + " , "

        table_columns = table_columns[:-2]  # remove the last ,

        create_table_query = f"Create Table if not exists {self.dbname}.{table_name}(" \
                             f"{table_columns})"

        db_response = self.execute_query(create_table_query, commit=True)
        # return self.is_table_exists(table_name)

    def insert_to_table(self, table_name, col_info, row_values, database_name= None):
        # if self.is_table_exists(table_name):
        if database_name:
            self.select_db(database_name)

        col_info = ['`' + s + '`' for s in col_info]
        insert_query = f"INSERT INTO {self.dbname}.{table_name} ({(','.join(col_info))}) " \
                               f"VALUES ({(', '.join(row_values))})"
        db_response = self.execute_query(insert_query, commit=True)

    def get_table_count(self, table_name):
        table_count_query = f"select count(1) from {self.dbname}.{table_name}"
        db_response = self.execute_query(table_count_query)
        return db_response


dbo = DbOperations(host="localhost", port=3306, user="root", password="laptop@123")

DBNAME = "CarbonNanotubes"
db_status = dbo.create_db(DBNAME)
if not db_status['status']:
    logging.critical("Exiting the application, cannot create the db")
    exit(1)

# dbo = DbOperations(host="localhost", port=3306, user="root", password="laptop@123", db_name="CarbonNanotubes")

TABLE_NAME = "carbon_nanotubes_info"

dbo.select_db(DBNAME)

# https://archive.ics.uci.edu/ml/datasets/Carbon+Nanotubes
# Dataset details and data available at the above URL

with open("carbon_nanotubes.csv", "r") as in_file:
    reader = csv.reader(in_file,delimiter=';')
    header = next(reader)
    print(header)
    dbo.create_table(TABLE_NAME, {"FLOAT (9,3)":header[:2], "VARCHAR(255)": header[2:]})
    for row_value in tqdm(reader):
        row_val = [u for u in row_value[:2]] + ['"' + t + '"' for t in row_value[2:]]
        dbo.insert_to_table(TABLE_NAME, header, row_val, DBNAME)
