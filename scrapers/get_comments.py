import requests
import json
import time
import pandas as pd


API_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"

def parse_comment(comment):
    comment = comment.replace("\n", " ")
    comment = comment.replace("<p>", " ")
    comment = comment.replace("</p>", " ")
    comment = comment.replace("<i>", " ")
    comment = comment.replace("</i>", " ")
    comment = comment.replace("&quot;", " ")


def main():
    post_ids = pd.read_csv("posts.csv").id

    with open("comments.csv", "w") as f:
        f.write("id,text\n")

        for post_id in post_ids: 
            response = requests.get(API_URL.format(id=post_id))
            comment_ids = response.json()["kids"]
            for comment_id in comment_ids:
                response = requests.get(API_URL.format(id=comment_id))
                try:
                    text = response.json()["text"]
                except:
                    continue
                f.write(str(comment_id) + ",\"" + text + "\"\n")
                time.sleep(1)
            return

        

if __name__ == "__main__":
    main() 
