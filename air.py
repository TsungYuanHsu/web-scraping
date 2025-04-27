import requests
import pprint
import re
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'air'

# Connect to server

try:
  cnx = mysql.connector.connect(user='root', password='typqsc15687', host='127.0.0.1')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    print('Successfully connect to MySQL server')
cursor = cnx.cursor()

# Create database if not existed

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# Create table

TABLES = {}
TABLES['location_aqi'] = (
    "CREATE TABLE `location_aqi` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `location` varchar(14) NOT NULL,"
    "  `aqi` int NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Insert data to table

add_location_aqi = ("INSERT INTO location_aqi "
               "(location, aqi) "
               "VALUES (%s, %s)")

r = requests.get('https://airtw.moenv.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2025042710.json?t=1745723985921')
if r.status_code == 200:
    print('Connection is ok')
    data = r.json()
    # name_aqi = [d for d in data if '富貴角' in d['Name']] [0] ['Name']
    # result = re.search(r'AQI=(\d+)', name_aqi).group(1)
    # # group(): return what regex can recognize
    # # group(1): return the first capture item
    # print(result)
    for d in data:
        try:
            location = re.search(r'(.+)\(AQI=(\d+)', d['Name']).group(1)
            aqi = re.search(r'(.+)\(AQI=(\d+)', d['Name']).group(2)
        except AttributeError:
            continue
        # print(location, aqi)
        data_location_aqi = (location, aqi)
        
        cursor.execute(add_location_aqi, data_location_aqi)
cnx.commit()

print('close')
cursor.close()
cnx.close()

