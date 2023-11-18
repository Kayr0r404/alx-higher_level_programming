#!/usr/bin/python3
'''lists all states with a name starting with N (upper N) from the database
Arguments:
    mysql_username, mysql_password and database_name'''

import sys
import MySQLdb as mysql

if __name__ == '__main__':
    usr, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    mydb = mysql.connect(host='localhost', user=usr,
                         passwd=psswd, db=db, port=3306)
    cursor = mydb.cursor()
    query = 'SELECT cities.id, cities.name, states.name'
    q2 = ' FROM cities'
    q3 = ' JOIN states ON cities.state_id = states.id'
    cursor.execute(query + q2 + q3)
    results = cursor.fetchall()

    for i in results:
        print(i)

    mydb.close()
