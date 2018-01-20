# coding: utf-8
import os
import os.path
import codecs

import json

from .idControl import Seriennummer

class Database(object):
    def __init__(self, database_name, size):

        self.data = None
        self.database_str = database_name + ".json"
        self.seriennr = Seriennummer(database_name)
        self.size = size
        self.readData()

        self.data_a = [
            {
                "id": "0",
                "col1": "default col1",
                "col2": "default col2"
            },
            {
                "id": "1",
                "col1": "Wert 1/1",
                "col2": "Wert 1/2"
            },
            {
                "id": "2",
                "col1": "Wert 2/1",
                "col2": "Wert 2/2"
            },
            {
                "id": "3",
                "col1": "Wert 3/1",
                "col2": "Wert 3/2"
            },
            {
                "id": "4",
                "col1": "Wert 4/1",
                "col2": "Wert 4/2"
            }
        ]

    def read_px(self, id_spl = None):
        data_o = None
        if id_spl == None:
            data_o = self.data_a
        else:
            id_i = int(id_spl)
            if id_i > 0 and  id_i < len(self.data_a):
                data_o = self.data_a[id_i]
            else:
                data_o = self.data_a[0]
        return data_o


    def create(self, newData):
        newId = self.seriennr.getNewID()
        self.data[newId] = newData
        self.saveData()
        return newId

    def read(self, id_spl=None):
        data = None
        if id_spl == None:
            data = self.data
        else:
            if id_spl in self.data:
                data = self.data[id_spl]
        return data

    def update(self, newData):
        if newData[0] in self.data:
            self.data[newData[0]] = newData[1:]
            self.saveData()

    def delete(self, entryId):
        if entryId in self.data:
            del self.data[entryId]
            self.saveData()

    def getIdList(self, dataList, pos):
        IdList = []
        data = []
        data.append(dataList)
        for i in data:
            for loop in self.data:
                if self.data[loop][pos] == i:
                    IdList.append(loop)
        return IdList

    def readData(self):
        try:
            fp = codecs.open(os.path.join('data', self.database_str), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            #self.data_o = {}
            newId = self.seriennr.getNewID()
            self.data = {newId: [''] * (self.size)}
            self.saveData()
        else:
            with fp:
                self.data = json.load(fp)
        return

    def saveData(self):
        with codecs.open(os.path.join('data', self.database_str), 'w', 'utf-8') as fp:
            json.dump(self.data, fp)

#wird nicht mehr benötigt:
    def entryExists(self, value):
        for item in self.data:
            if self.data[item][0] == value:
                return True
        return False
#end benötigt

    def getEntryID(self, data, pos = 0):
        for item in self.data_o:
            if item != 0:
                if self.data_o[item][pos] == data:
                    return item
        return -1

# EOF
