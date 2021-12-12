#/usr/bin/python3
import sqlite3
import requests

def get_rss_data():
    r = requests.get('https://hnrss.org/newest?points=100')
    print(r.text)



def main():
    db = sqlite3.connect('hn_glasses.db')
    db.execute('''INSERT INTO  posts (id) VALUES (123)''')
    #print(db.execute('''SELECT * FROM posts''').fetchall())
    get_rss_data()



if __name__ == '__main__':
    main()
