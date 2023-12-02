#!/usr/bin/python3
"""a script that takes in an argument and
displays all values in the states"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name \
    LIKE BINARY '{}' ORDER BY states.id".format(
        sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
