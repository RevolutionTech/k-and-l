import ast
import datetime
import json
import os

MESSAGES_DIR = "messages"

def get_sorted_filenames():
    filenames = os.listdir(MESSAGES_DIR)
    return sorted(filenames, key=lambda fn: int(fn.split(".")[0].split("_")[-1]))

def get_message_dt(message):
    timestamp = message["timestamp_ms"] / 1000.0
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.replace(microsecond=0).isoformat()

def import_messages():
    print("Importing messages...")

    messages = []
    for filename in get_sorted_filenames():
        with open(f"messages/{filename}", "r") as f:
            file_content = f.read()
            file_json = json.loads(file_content)
            messages += file_json["messages"]

    print(f"Import successful! Messages range from {get_message_dt(messages[-1])} to {get_message_dt(messages[0])}.")

    return messages

def find_word(messages, word):
    num_occurrences = 0

    for message in messages:
        content = message.get("content")
        if content:
            num_occurrences += content.count(word)

    return num_occurrences

def runscript():
    messages = import_messages()
    word = input("Word to search: ")
    unescaped_word = ast.literal_eval('"' + word + '"')
    num_occurrences = find_word(messages, unescaped_word)
    print(f"The word {unescaped_word} appeared {num_occurrences} times in messages.")


if __name__ == "__main__":
    runscript()
