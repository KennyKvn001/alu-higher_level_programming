#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table 
of hbtn_0e_0_usa whose name matches the argument.
   usage : ./2-my_filter_states.py <mysql username>\
                                   <mysql passwd>\
                                   <database name>\
                                   <state name searched>
"""
import sys
import MySQLdb

if __name__ = '__main__':

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT *\
            FROM tables\
            WHERE BINARY name = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]