#!/usr/bin/python3
'''lists all cities in a state with a name starting
with N (uppercase N) from the database
Arguments:
    mysql_username, mysql_password, database_name, and state_name'''

import sys
import MySQLdb as mysql

if __name__ == '__main__':
    usr, psswd = sys.argv[1], sys.argv[2],
    db, search = sys.argv[3], sys.argv[4]

    mydb = mysql.connect(host='localhost', user=usr,
                         passwd=psswd, db=db, port=3306)
    cursor = mydb.cursor()

    # Use parameterized query to avoid SQL injection
    query = 'SELECT cities.name \
        FROM cities \
            JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s'
    cursor.execute(query, (search,))

    results = cursor.fetchall()

    for i in range(len(results)):
        print(results[i][0], end='')
        if i < len(results) - 1:
            print(', ', end='')
    print()

    mydb.close()
