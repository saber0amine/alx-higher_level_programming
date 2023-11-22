#!/usr/bin/python3
""" list all cities with given state name """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("""
        SELECT c.name
        FROM cities AS c LEFT JOIN states AS s
        ON c.state_id = s.id
        WHERE s.name = %s
        ORDER BY c.id;
        """, (sys.argv[4],))
    print(", ".join([c[0] for c in cur.fetchall()]))
