#!/usr/bin/python3
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="JSON file from takeout of Google Chat", type=str)
args = parser.parse_args()

f = open(args.filename)

data = json.load(f)

for message in data["messages"]:
    if "created_date" not in message:
        if "text" not in message:
            print(f"""{message["creator"]["name"]}\n""")
        else:
            print(f"""{message["creator"]["name"]}\n{message["text"]}\n""")
    else:
        if "text" not in message:
            print(f"""{message["created_date"]}\n{message["creator"]["name"]}\n""")
        else:
            print(
                f"""{message["created_date"]}\n{message["creator"]["name"]}\n{message["text"]}\n"""
            )
f.close()
