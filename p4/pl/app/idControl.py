# coding: utf-8

import os
import os.path
import codecs

import json

class Seriennummer(object):
    def __init__(self, database_name):
        self.database_str = "Numbers.json"
        self.data = {}
        self.readData()
        self.database_name = database_name
        if self.database_name not in self.data:
            self.data[self.database_name] = 1
        self.saveData()

    def getNewID(self):
        thisid = self.data[self.database_name]
        self.data[self.database_name] = thisid + 1
        self.saveData()
        return thisid

    def readData(self):
        try:
            fp = codecs.open(os.path.join('data', self.database_str), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            self.data = {}
            #self.data = {"0":['1'] + [''] * (self.size - 1)}
            self.saveData()
        else:
            with fp:
                self.data = json.load(fp)
        return

    def saveData(self):
        with codecs.open(os.path.join('data', self.database_str), 'w', 'utf-8') as fp:
            json.dump(self.data, fp)

# EOF
