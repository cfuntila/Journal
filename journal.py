#!/usr/bin/env python3

import argparse
import json
import os

class Entry:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def isValidEntry(self):
        return len(self.title) > 0 and len(self.content) > 0

    def getContent(self):
        return self.content
    
    def getTitle(self):
        return self.title

class Journal:

    def __init__(self, fileName):
        self.fileName = fileName
        self.myIndent = 4
    
    def addEntry(self, title, content):
        newEntry = Entry(title, content)
        
        if not os.path.isfile(self.fileName):
            firstEntry = [ newEntry.__dict__ ]
            with open(self.fileName, mode='w') as f:
                f.write(json.dumps(firstEntry, indent=self.myIndent))
        else:
            # TODO - O(n) -> make O(1) : find a way to append 
            with open(self.fileName) as f:
                currData = json.load(f)

            currData.append(newEntry.__dict__)

            with open(self.fileName, mode='w') as f:
                f.write(json.dumps(currData, indent=self.myIndent))

    def printJournalTitles(self):
        if not os.path.isfile(self.fileName):
            print("\nNo entries in journal, nothing to print\n")
        else:
            with open(self.fileName) as f:
                # currData is a dictionary
                currData = json.load(f)

            print("\nYour Entry Titles:")
            print("==================")
            for i in range(len(currData)):
                entry = currData[i]
                print(f"{i+1}. {entry['title']}")
            print("\n")

    # prints the contents of the json file, used for testing
    def printJournal(self):
        if not os.path.isfile(self.fileName):
            print("No entries in journal, nothing to print")
        else:
            with open(self.fileName) as f:
                data = f.read()
                print(data)    

def main():
    parser = argparse.ArgumentParser(description="Journal Entry Tracker")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-c", "--create", help="the contents")
    parser.add_argument("--title", help="the title")
    group.add_argument("-l", "--list", help="List entries", action="store_true")

    args = parser.parse_args()

    if args.list:
        myJournal.printJournalTitles()
    elif args.create:
        myJournal.addEntry(args.title, args.create)
    else:
        print("You must povide an action: create entry or list entries")

if __name__ == '__main__':
    myJournal = Journal("data.json")
    main()


