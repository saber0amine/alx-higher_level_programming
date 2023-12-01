#!/usr/bin/python3
"""lists all cities based on a name"""
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
    query = "SELECT cities.name FROM cities \
    INNER JOIN states ON states.id=cities.state_id \
    WHERE states.name=%s"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(map(lambda row: row[0], rows))
    print(*tmp, sep=", ")
    cur.close()
    conn.close()
