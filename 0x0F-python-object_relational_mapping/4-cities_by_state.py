#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = con.cursor()
    c.execute("SELECT cities.id, cities.name, states.name \
              FROM cities JOIN states ON cities.state_id \
              = states.id ORDER BY cities.id ASC")
    ss = c.fetchall()
    for s in ss:
        print(s)
    c.close()
    con.close()
