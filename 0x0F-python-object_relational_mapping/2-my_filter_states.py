#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = con.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
              ORDER BY id ASC".format(sys.argv[4]))
    ss = c.fetchall()
    for s in ss:
        print(s)
    c.close()
    con.close()
