#!/usr/bin/env python3

import unittest
import os
import json

class TestJournal(unittest.TestCase):
            
    @classmethod
    def tearDownClass(cls):
        os.remove("data.json")

    def test_expected_create_1(self):
        # print('in test 1')
        os.system("./journal.py --title \"ttt\" --create \"ccccc\"")
        with open("data.json") as f:
            currData = json.load(f)
        
        self.assertTrue(currData[-1]["title"] == "ttt" )
    
    def test_expected_create_2(self):
        # print('in test 2')
        os.system("./journal.py --create \"ccccc\" --title \"newttt\"")
        with open("data.json") as f:
            currData = json.load(f)
        self.assertTrue(currData[-1]["title"] == "newttt" )
   

if __name__ == '__main__':
    unittest.main()