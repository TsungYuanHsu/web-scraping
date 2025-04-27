import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'air'

# Connect to server

try:
    cnx = mysql.connector.connect(user='root', password='typqsc15687', host='127.0.0.1', database=DB_NAME)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
else:
    print('Successfully connect to MySQL server')
cursor = cnx.cursor(dictionary=True)

query = ("SELECT * FROM location_aqi "
         "WHERE aqi > 100")

cursor.execute(query)

# for id, location, aqi in cursor:
#     print("{}:{}, and aqi is {}".format(id, location, aqi))

for row in cursor:
    print(row)

print('closing')
cursor.close()
cnx.close()