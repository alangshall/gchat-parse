#!/usr/bin/python3
"""This program takes a Google Chat Takeout JSON file and returns the contents of a conversation."""
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="JSON file from takeout of Google Chat", type=str)
args = parser.parse_args()

with open(args.filename, encoding="utf-8") as f:
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
