#!/usr/bin/python3
'''lists all states with a name starting with N (upper N) from the database
Arguments:
    mysql_username, mysql_password and database_name'''

import sys
import MySQLdb as mysql

if __name__ == '__main__':
    usr, passwd = sys.argv[1], sys.argv[2]
    db, search = sys.argv[3], sys.argv[4]
    mydb = mysql.connect(host='localhost', user=usr,
                         passwd=passwd, db=db, port=3306)
    cursor = mydb.cursor()
    query = 'SELECT * FROM states WHERE name \
        LIKE %s  ORDER BY id ASC'.format(search)
    cursor.execute(query, ('{}%'.format(search),))
    results = cursor.fetchall()

    for i in results:
        print(i)

    mydb.close()
