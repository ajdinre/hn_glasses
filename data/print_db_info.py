#/usr/bin/python3
import sqlite3
import requests
import re


def main():
    db = sqlite3.connect('hn_glasses.db')
    ids = db.execute('''SELECT * FROM posts''').fetchall()
    print('ids:', ids)
    print('len:', len(ids))


if __name__ == '__main__':
    main()
