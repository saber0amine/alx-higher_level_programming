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
    query = 'SELECT cities.name\
            FROM cities\
            JOIN states\
            ON cities.state_id=states.id\
            WHERE states.name\
            LIKE %s;'
    cursor.execute(query, (s_name + '%',))

    cities = cursor.fetchall()
    i = 0
    for city in cities:
        if i > 0:
            print(", ", end="")
        print('%s' % city, end="")
        i += 1
    print("")

    cursor.close()
    db.close()
