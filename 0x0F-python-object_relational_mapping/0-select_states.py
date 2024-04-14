#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = con.cursor()
    c.excute("SELECT * FROM states ORDER BY id ASC")
    ss = c.fetchall()
    for s in ss:
        print(s)
    c.close()
    db.close()
