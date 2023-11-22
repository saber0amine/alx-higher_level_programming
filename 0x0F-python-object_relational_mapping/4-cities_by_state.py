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
    cursor.execute('SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    JOIN states\
                    ON states.id = cities.state_id\
                    ORDER BY cities.id ASC;')

    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db.close()
