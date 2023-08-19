#!/usr/bin/python3
"""
This script that lists all `states` with a `name` starting
with `N` (upper N) from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Making connection and accessing the database with MySQLdb.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""
                SELECT * FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY states.id ASC
                """)
    rows = cur.fetchall()

    for row in rows:
        print(row)
