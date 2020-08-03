#!/usr/bin/env python3

import unittest
import os
import json

class TestJournal(unittest.TestCase):
            
    @classmethod
    def tearDownClass(cls):
        os.remove("data.json")

    def test_expected_create_1(self):
        title = "ttt"
        content = "ccc"
        os.system(f"./journal.py --title {title} --create {content}")

        with open("data.json") as f:
            currData = json.load(f)
        
        self.assertTrue(currData[-1]["title"] == title)
        self.assertTrue(currData[-1]["content"] == content)
    
    def test_expected_create_2(self):
        title = "newTTT"
        content = "newCCC"
        os.system(f"./journal.py --create {content} --title {title}")

        with open("data.json") as f:
            currData = json.load(f)

        self.assertTrue(currData[-1]["title"] == title)
        self.assertTrue(currData[-1]["content"] == content)
    
    def test_unexpected_title_no_content(self):
        title = "addedOnlyTitle"
        os.system(f"./journal.py --title {title}")

        with open("data.json") as f:
            currData = json.load(f)

        self.assertTrue(currData[-1]["title"] != title)
    
    def test_unexpected_content_no_title(self):
        
        content = "addedOnlyContent"
        os.system(f"./journal.py --create {content}")

        with open("data.json") as f:
            currData = json.load(f)

        self.assertTrue(currData[-1]["content"] != content)
    
    def test_unexpected_empty_content_empty_title(self):
        os.system("./journal.py --create \" \" --title \" \" ")

        with open("data.json") as f:
            currData = json.load(f)
        
        self.assertTrue(currData[-1]["title"] != " ")
        self.assertTrue(currData[-1]["content"] != " ")
    
    def test_unexpected_multiple_entries_same_title(self):
        title = "sameTitle"
        content1 = "content1"
        content2 = "content2"

        os.system(f"./journal.py --title {title} --create {content1}")
        os.system(f"./journal.py --title {title} --create {content2}")

        with open("data.json") as f:
            currData = json.load(f)

        self.assertTrue(currData[-1]["title"] == title)
        self.assertTrue(currData[-2]["title"] != title)

if __name__ == '__main__':
    unittest.main()