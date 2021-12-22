import requests
import json
import time
import pandas as pd


API_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"


def main():
    post_ids = pd.read_csv("../data/hn_posts_500.csv").id

    with open("data.csv", "w") as f:
        f.write("id,comment count\n")
    
        c = 0
        for post_id in post_ids: 
            response = requests.get(API_URL.format(id=post_id))
            comment_size = len(response.json()["kids"])
            print(c)
            c += 1
            f.write(str(post_id) + "," + str(comment_size) + "\n")
            time.sleep(0.5)

        

if __name__ == "__main__":
    main() 
