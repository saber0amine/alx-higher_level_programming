#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa"""

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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
