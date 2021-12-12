#/usr/bin/python3
import sqlite3
import requests
import re


def get_ids_from_rss():
    r = requests.get('https://hnrss.org/newest?points=100')
    ids = set()
    for relative_url in re.findall( r'item\?id=[0-9]*', r.text):
        ids.add(int(relative_url[8:]))
    return ids


def main():
    db = sqlite3.connect('hn_glasses.db')
    #print(db.execute('''SELECT * FROM posts''').fetchall())
    ids = get_ids_from_rss()

    insert_query = "INSERT INTO  posts (id) VALUES (?)"

    for identifier in ids:
        print(identifier)
        try:
            db.execute(insert_query, (identifier,))
        except: # Already exists
            pass
    db.commit()


if __name__ == '__main__':
    main()
