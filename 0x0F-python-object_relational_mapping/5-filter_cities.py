#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists 
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = con.cursor()
    c.execute("SELECT cities.id, cities.name FROM cities \
              JOIN states ON cities.state_id = states.id \
              WHERE states.name LIKE BINARY %(s_name)s \
              ORDER BY cities.id ASC", {'s_name': sys.argv[4]})
    ss = c.fetchall()
    for s in ss:
        print(s)
    c.close()
    con.close()
