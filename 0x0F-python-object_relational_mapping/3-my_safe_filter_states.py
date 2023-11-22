#!/usr/bin/python3
''' lists all states '''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost'
    )
    cursor = db.cursor()
    s_name = sys.argv[4]
    query = 'SELECT * FROM states WHERE states.name LIKE %s'
    cursor.execute(query, (s_name + '%',))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
