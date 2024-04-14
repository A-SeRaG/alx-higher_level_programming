#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = con.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
              ORDER BY id ASC", {'name': sys.argv[4]})
    ss = c.fetchall()
    for s in ss:
        print(s)
