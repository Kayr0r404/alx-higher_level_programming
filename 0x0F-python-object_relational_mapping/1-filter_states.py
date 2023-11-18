#!/usr/bin/python3
'''lists all states with a name starting with N (upper N) from the database
Arguments:
    mysql_username, mysql_password and database_name'''

import sys
import MySQLdb as mysql

usr, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
mydb = mysql.connect(host='localhost',
                     user=usr,
                     passwd=password,
                     db=database,
                     port=3306)
cursor = mydb.cursor()
query = 'SELECT * FROM states WHERE name LIKE \'N%\' ORDER BY id ASC'
cursor.execute(query)
results = cursor.fetchall()

for i in results:
    print(i)

mydb.close()
