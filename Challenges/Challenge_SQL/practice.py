import mysql.connector as connection

# query1 = "use CarbonNanotubes;"
# query2 = " show tables;"
query1 = "Create database CarbonNanotubes;"
# query2 = "show databases;"

host = "localhost"
user = "root"
port = 3306
password = "laptop@123"
dbname = "CarbonNanotubes"

dbConnection = connection.connect(
                    host=host, port = port, user=user, password=password)
cursor = dbConnection.cursor()
print(query1.split(';'))
# cursor.execute(query1)
# cursor.execute(query2)

# cursor.execute(query, multi=True)

# print(cursor.fetchall())
# import time
# time.sleep(30)
#
# dbConnection = connection.connect(
#                     host=host, port = port, user=user, password=password, database=dbname)
# query = "show databases;"
# cursor = dbConnection.cursor()
# cursor.execute(query)
# print(cursor.fetchall())
# time.sleep(30)
