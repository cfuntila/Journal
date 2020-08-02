#!/usr/bin/env python3

import argparse
import json
import os

class Entry:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def isValidEntry(self):
        self.title, self.content = self.title.strip(), self.content.strip()
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
        if not newEntry.isValidEntry(): 
            print("\nYou must enter both a title and content of length > 0\n")
            return
        if not os.path.isfile(self.fileName):
            firstEntry = [ newEntry.__dict__ ]
            with open(self.fileName, mode='w') as f:
                f.write(json.dumps(firstEntry, indent=self.myIndent))
        else:
            # TODO - O(n) -> make O(1) : find a way to append 
            with open(self.fileName) as f:
                currData = json.load(f)

            if self.entryExists(newEntry, currData):
                print("\nYou already have a journal entry with the same title\n")
                return

            currData.append(newEntry.__dict__)

            with open(self.fileName, mode='w') as f:
                f.write(json.dumps(currData, indent=self.myIndent))

    # O(n), checks if there is a journal entry with the same name as the new one a user wants to add
    def entryExists(self, entry, currData):
        for i in range(len(currData)):
                currEntry = currData[i]
                if currEntry['title'] == entry.title:
                    return True
        return False

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
            print("\nNo entries in journal, nothing to print\n")
        else:
            with open(self.fileName) as f:
                data = f.read()
                print(data)    

def main(myJournal):
    parser = argparse.ArgumentParser(description="Journal Entry Tracker")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-c", "--create", help="the contents")
    parser.add_argument("-t", "--title", help="the title")
    group.add_argument("-l", "--list", help="List entries", action="store_true")

    args = parser.parse_args()

    if args.list:
        myJournal.printJournalTitles()
    elif args.create and args.title:
        myJournal.addEntry(args.title, args.create)
    else:
        print("\nYou must provide an action: create entry with both a title and content or list entries. Use --help for help.\n")
        # raise RuntimeError('You must provide an action: create entry with both a title and content or list entries. Use --help for help.')
        
if __name__ == '__main__':
    myJournal = Journal("data.json")
    main(myJournal)
    


