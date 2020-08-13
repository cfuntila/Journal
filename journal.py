#!/usr/bin/env python3

import argparse
import json
import os
import math
from entry import Entry

class Journal:

    def __init__(self, fileName):
        self.fileName = fileName
        self.myIndent = 4

    def getNextValidID(self):
        if not os.path.isfile(self.fileName):
            return 1
        else:
            currData = self.getEntriesFromFile()
            
            if not currData:
                return 1
            else: 
                lastID = currData[-1]['id']
                return lastID + 1

    def getEntriesFromFile(self):
        with open(self.fileName) as f:
                currData = json.load(f)
        return currData

    def writeEntriesToFile(self, data):
        with open(self.fileName, mode='w') as f:
            f.write(json.dumps(data, indent=self.myIndent))

    def addEntry(self, title, content):
        id = self.getNextValidID()

        newEntry = Entry(title, content, id)
        if not newEntry.isValidEntry(): 
            print("\nYou must enter both a title and content of length > 0\n")
            return

        if not os.path.isfile(self.fileName):
            newData = [ newEntry.__dict__ ]
        else:
            newData = self.getEntriesFromFile()
            newData.append(newEntry.__dict__)        
        self.writeEntriesToFile(newData)
    
    # Note: not used anymore: Instead deleteEntryByID will be called upon deletion
    def deleteEntry(self, title):
        if not os.path.isfile(self.fileName):
            print("\nno file, nothing to delete\n")
            return
        else:
            found = False
            currData = self.getEntriesFromFile()
            
            for i in range(len(currData)):
                element = currData[i]
                if element['title'] == title:
                    currData.pop(i)
                    found = True
                    break
            if not found: 
                print(f"\nEntry with title {title} not found\n")
            else:   
                self.writeEntriesToFile(currData)
    
    def deleteEntryByID(self, idGivenByUser):
        if not os.path.isfile(self.fileName):
            print("\nno file, nothing to delete\n")
            return
        else:
            currData = self.getEntriesFromFile()
            # for i in range(len(currData)):
            #     element = currData[i]
            #     if element['id'] == idGivenByUser:
            #         currData.pop(i)
            #         break
            currData.pop(idGivenByUser-1)
            self.writeEntriesToFile(currData)

    def update(self, idGivenByUser, newTitle):
        if not os.path.isfile(self.fileName):
            print("\nno file, nothing to update\n")
            return
        else:
            foundIdGivenByUser = False
            currData = self.getEntriesFromFile()

            element = self.getElementByID(idGivenByUser, currData)

            if element:
                foundIdGivenByUser = True
                element['title'] = newTitle

            if not foundIdGivenByUser:
                print("\nThe id you provided does not exist in the journal\n")
            else:
                self.writeEntriesToFile(currData)

    def getElementByID(self, id, currData):
        for i in range(len(currData)):
            element = currData[i]
            if element['id'] == id:
                return element

    def contains(self, currentValue, userSearchValue):
        currentValue, userSearchValue = currentValue.lower(), userSearchValue.lower()
        return userSearchValue in currentValue        

    def search(self, attributeType, value):
        if not os.path.isfile(self.fileName):
            print("\nno file, nothing to search for\n")
            return
        else:
            currData = self.getEntriesFromFile()
            res = []
            for i in range(len(currData)):
                if not attributeType:
                    if self.contains(currData[i]['content'], value) or self.contains(currData[i]['title'], value):
                        res.append(currData[i])
                else:
                    if self.contains(currData[i][attributeType], value):
                        res.append(currData[i])
            self.printDictionaryTitlesAndContent(res)

    # O(n), checks if there is a journal entry with the same name as the new one a user wants to add
    def entryExists(self, entry, currData):
        for i in range(len(currData)):
                currEntry = currData[i]
                if currEntry['title'] == entry.title:
                    return True
        return False
    

    # Print Functions
    def printJournalTitles(self):
        if not os.path.isfile(self.fileName):
            print("\nNo entries in journal, nothing to print\n")
        else:
            currData = self.getEntriesFromFile()
            self.printDictionaryTitles(currData)
    
    def printJournalTitlesAndContent(self):
        if not os.path.isfile(self.fileName):
            print("\nNo entries in journal, nothing to print\n")
        else:
            currData = self.getEntriesFromFile()
            self.printDictionaryTitlesAndContent(currData)
    
    def printDictionaryTitles(self, myDict):
        print("\nYour Entry Titles:")
        print("==================")
        for i in range(len(myDict)):
            entry = myDict[i]
            print(f"{i+1}. {entry['title']}, entry id: {entry['id']}")
        print("\n")

    def printDictionaryTitlesAndContent(self, myDict):
        print("\nYour Entries:")
        print("==================")
        for i in range(len(myDict)):
            entry = myDict[i]
            print(f"{i+1}. Title: {entry['title']}")
            print(f"   Content: {entry['content']}")
            print(f"   Entry id: {entry['id']}")
        print("\n")

    # ===== Functions used for Testing ===================
    # prints the contents of the json file, used for testing
    def printJournal(self):
        if not os.path.isfile(self.fileName):
            print("\nNo entries in journal, nothing to print\n")
        else:
            with open(self.fileName) as f:
                data = f.read()
                print(data)    




def parseArguments():
    parser = argparse.ArgumentParser(description="Journal Entry Tracker")
    group = parser.add_mutually_exclusive_group()

    
    parser.add_argument("-t", "--title",       metavar='', help="The title")
    parser.add_argument("-n", "--new",         metavar='', help="New title")
    parser.add_argument("-a", "--attribute",   metavar='', help="Attribute type: 'title'/'content'")
    group.add_argument("-c",  "--create",      metavar='', help="The contents")
    group.add_argument("-d",  "--delete",      metavar='', help="Delete an entry")
    group.add_argument("-s",  "--search",      metavar='', help="Search for a string in all entries")
    group.add_argument("-i",  "--changeTitle", metavar='', help="Enter the id number of the entry you want to change")
    group.add_argument("-l",  "--list",        action="store_true", help="List entries")
    group.add_argument("-v",  "--verbose" ,    action="store_true", help="List out both title and content")

    args = parser.parse_args()

    return args

def completeUserActions(args, myJournal):
    if args.list:
        myJournal.printJournalTitles()
    elif args.verbose:
        myJournal.printJournalTitlesAndContent()
    elif args.create and args.title:
        myJournal.addEntry(args.title, args.create)
    elif args.delete:
        myJournal.deleteEntryByID(int(args.delete))
    elif args.search:
        myJournal.search(args.attribute, args.search)
    elif args.changeTitle and args.new:
        myJournal.update(int(args.changeTitle), args.new)
    else:
        print("\nYou must provide an action: create entry with both a title and content or list entries. Use --help for help.\n")
        
def main():
    myJournal = Journal("data.json")
    args = parseArguments()
    completeUserActions(args, myJournal)

if __name__ == '__main__':
    main()