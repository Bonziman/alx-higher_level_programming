#!/usr/bin/python3
"""a script to list all states from a database"""
import MySQLdb
import sys


def main():
    """entry function"""
    MY_HOST = 'localhost'
    MY_PORT = 3306
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    try:
        db = MySQLdb.connect(host=MY_HOST, port=MY_PORT, user=MY_USER,
                             passwd=MY_PASS, db=MY_DB)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE NAME LIKE \
                        BINARY 'N%'ORDER BY id ASC")

        states = cursor.fetchall()
        for state in states:
            print("({}, '{}')".format(state[0], state[1]))

    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
