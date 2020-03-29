#!/usr/bin/python3
"""lists the searched state from the database hbtn_0e_0_usa"""
import sys
import MySQLdb
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        if query_rows[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
