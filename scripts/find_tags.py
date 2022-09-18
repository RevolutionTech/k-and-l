import json
import os
from collections import Counter


POSTS_DIR = os.path.join("scratch", "posts")


def runscript():
    tagged_posts = Counter()

    filename = input("Filename to search: ")
    while filename:
        with open(os.path.join(POSTS_DIR, filename), "r") as f:
            file_content = f.read()
        file_json = json.loads(file_content)

        for post in file_json:
            if "tags" in post and "attachments" in post and any(any("media" in item for item in attachment["data"]) for attachment in post["attachments"]):
                tagged_posts.update(tag["name"] for tag in post["tags"])

        filename = input("Add another filename [blank to continue]: ")

    print("Tags found: ", tagged_posts)


if __name__ == "__main__":
    runscript()
