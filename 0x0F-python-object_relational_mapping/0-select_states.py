#!/usr/bin/python3
import MySQLdb
from sys import argv

if__name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    ur = db.cursor()
    ur.execute("SELECT * FROM states")
    srow = ur.fetchall()
    for row in srow:
        print(row)
    ur.close()
    db.close()


