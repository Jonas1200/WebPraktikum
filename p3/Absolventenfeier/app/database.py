# coding: utf-8

import os
import os.path
import codecs

import json

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

    #-------------------------------------------------------
    def __init__(self, database_str, size):
    #-------------------------------------------------------
        #database_str, size
        self.data_o = None
        self.database_str = database_str
        self.size = size
        self.readData_p()

    #-------------------------------------------------------
    def create_px(self, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!

        # 'freien' Platz suchen,
        # falls vorhanden: belegen und Nummer des Platzes als Id zurückgeben


        #id_s = 1
        #while id_s in self.data_o:
        #    id_s += 1
        #id_s = str(id_s)

        id_s = str(self.getNewCurrentID())
        self.data_o[id_s] = data_opl
        self.saveData_p()
        #
        #
        # self.data_o[id_s] = data_opl
        # for loop_i in range(0, 15):
        #     if self.data_o[str(loop_i)][0] == '':
        #         id_s = str(loop_i)
        #         self.data_o[id_s] = data_opl
        #         self.saveData_p()
        #         break
        #
        # return id_s
        #
        # if not data_opl[0] in self.data_o:
        #     self.data_o[data_opl[0]] = data_opl[1:]
        # self.saveData_p()
        #return data_opl[0]
        return id_s

    #-------------------------------------------------------
    def getNewCurrentID(self):
        id_s = self.data_o[str(0)][0]
        self.data_o[str(0)][0] = int(id_s) + 1
        return id_s

    #-------------------------------------------------------
    def read_px(self, id_spl=None):
    #-------------------------------------------------------
        # hier zur Vereinfachung:
        # Aufruf ohne id: alle Einträge liefern
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            if id_spl in self.data_o:
                data_o = self.data_o[id_spl]

        return data_o

    #-------------------------------------------------------
    def update_px(self, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!
        if data_opl[0] in self.data_o:
            self.data_o[data_opl[0]] = self.data_o[data_opl[0]][:-(self.size-1)] + data_opl[1:]
            self.saveData_p()
    
    #-------------------------------------------------------
    def updateFB_px(self, data_opl):
    #-------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!
        if data_opl[0] in self.data_o:
            self.data_o[data_opl[0]] = self.data_o[data_opl[0]][:-(self.size-1)] + data_opl[1:] + self.data_o[data_opl[0]][self.size-1:]
            self.saveData_p()    
    
    #-------------------------------------------------------
    def delete_px(self, entry, isId=True):
    #-------------------------------------------------------
        if not isId:
            entry = self.getEntryID(entry)
        if entry in self.data_o:
            del self.data_o[entry]
            self.saveData_p()
            # hier müssen Sie den Code ergänzen
            # Löschen als Zurücksetzen auf die Default-Werte implementieren

            # Ihre Ergänzung

    # -------------------------------------------------------
    def getIdList(self, dataList, pos):
    # -------------------------------------------------------
        IdList = []
        data = []
        data.append(dataList)
        for i in data:
            for loop in self.data_o:
                if loop != '0':
                    if self.data_o[loop][pos] == i:
                        IdList.append(loop)
     #       bla=self.getEntryID(data[loop], pos1)
      #      IdList.append(self.getEntryID(data[loop], pos1))
        return IdList

#-------------------------------------------------------
    def getDefault_px(self):
    #-------------------------------------------------------
        
        return [''] * self.size # HIER müssen Sie eine Ergänzung vornehmen

    #-------------------------------------------------------
    def readData_p(self):
    #-------------------------------------------------------
        try:
            fp_o = codecs.open(os.path.join('data', self.database_str), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            #self.data_o = {}
            self.data_o = {"0":['1'] + [''] * (self.size - 1)}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)

        return

    #-------------------------------------------------------
    def saveData_p(self):
    #-------------------------------------------------------
        with codecs.open(os.path.join('data', self.database_str), 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o)

    #-------------------------------------------------------
    def entryExists_px(self, value):
    #-------------------------------------------------------
        for item in self.data_o:
            if item != '0':
                if self.data_o[item][0] == value:
                    return True
        return False
    #-------------------------------------------------------
    def passwordValidation(self, email, password):
    #-------------------------------------------------------
        for item in self.data_o:
            if self.data_o[item][0] == email and self.data_o[item][1] == password:
                return True
        return False
    # -------------------------------------------------------
    def getEntryID(self, data, pos = 0):
    # -------------------------------------------------------
        for item in self.data_o:
            if item != 0:
                if self.data_o[item][pos] == data:
                    return item
        return -1
# EOF