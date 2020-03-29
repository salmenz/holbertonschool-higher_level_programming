#!/usr/bin/python3
"""lists all cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities JOIN\
                ON states cities.state_id = states.id ORDER BY cities.id")
    query_rows = cur.fetchall()
    list = ""
    for row in query_rows:
        if row[1] == sys.argv[4]:
            list + row[0]
            list + ", "
    if list:
        print(list[:-2])
    cur.close()
    conn.close()
