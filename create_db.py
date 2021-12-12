#/usr/bin/python3
import sqlite3


def main():
    db = sqlite3.connect('hn_glasses.db')
    db.execute('''CREATE TABLE posts(id int PRIMART KEY UNIQUE)''')


if __name__ == '__main__':
    main()
