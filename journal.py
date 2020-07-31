#!/usr/bin/env python3

import argparse
import sys
import json
import pprint
import os


def parseArguments():
    parser = argparse.ArgumentParser(description="Journal Entry Tracker")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--create", help="the contents", default="contents")
    parser.add_argument("--title", help="the title", default="title")
    group.add_argument("-l", "--list", help="List entries", action="store_true")
    args = parser.parse_args()
    
    if args.list:
        # print("List out the entries")
        return ["List"]
    if args.create:
        # print("Title: {}".format(args.title,))
        # print("Contents: {}".format(args.create))
        return [args.title, args.create]

def printEntries():
    with open('data_file.json') as f:
        data = f.read()
        json_data = json.loads(data)
    print(json.dumps(json_data, indent=4, sort_keys=True))

def addEntry(title, contents):
    entries = []
    journalEntry = {title: contents}
    if not os.path.isfile("data_file.json"):
        entries.append(journalEntry)
        with open("data_file.json", mode='w') as f:
            f.write(json.dumps(entries, indent=2))
    else:
        # TODO - O(n) -> make O(1) : find a way to append 
        with open("data_file.json") as feedsjson:
            feeds = json.load(feedsjson)

        feeds.append(journalEntry)
        with open("data_file.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2))

def main():
    # args = [print entries] or [title, content]
    args = parseArguments()

    # list out the entries
    if len(args) <= 1:
        printEntries()
    # add an entry
    elif len(args) >= 2:
        title = args[0]
        contents = args[1]
        addEntry(title, contents)

main()


