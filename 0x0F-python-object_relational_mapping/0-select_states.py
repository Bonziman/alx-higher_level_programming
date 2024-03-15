#!/usr/bin/python3
"""a script to list all states from a database"""
import MySQLdb
import sys

def main():
    """main function"""
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1] , passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print("({}, '{}')".format(state[0], state[1]))
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
