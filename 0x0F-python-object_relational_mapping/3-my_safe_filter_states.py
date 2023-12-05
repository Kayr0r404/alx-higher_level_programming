#!/usr/bin/python3
'''takes in an argument and displays all values in the states table of db
 where name matches the argument
Arguments:
    mysql_username, mysql_password, database_name and state_name_searched'''

import sys
import MySQLdb as mysql

if __name__ == '__main__':
    usr, passwd = sys.argv[1], sys.argv[2]
    db, search = sys.argv[3], sys.argv[4]
    mydb = mysql.connect(host='localhost', user=usr,
                         passwd=passwd, db=db, port=3306)
    cursor = mydb.cursor()
    query = 'SELECT * FROM states WHERE name \
        LIKE BINARY %s  ORDER BY id ASC'
    cursor.execute(query, ('{}%'.format(search),))
    results = cursor.fetchall()

    for i in results:
        print(i)

    mydb.close()
