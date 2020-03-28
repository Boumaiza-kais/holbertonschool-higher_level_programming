#!/usr/bin/python3
#script that lists all states with a name starting with N (upper N)

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()
    statement = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    cursor.execute(statement)
    out = cursor.fetchall()
    for row in out:
        print(row)
    cursor.close()
    db.close()
