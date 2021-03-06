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

        if not data_opl[0] in self.data_o:
            self.data_o[data_opl[0]] = data_opl[1:]
        self.saveData_p()
        return data_opl[0]

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
    def delete_px(self, entry):
    #-------------------------------------------------------
        if entry in self.data_o:
            del self.data_o[entry]
            self.saveData_p()
            # hier müssen Sie den Code ergänzen
            # Löschen als Zurücksetzen auf die Default-Werte implementieren

            # Ihre Ergänzung

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
            self.data_o = {}
            #self.data_o = {"0":[''] * self.size}
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
        if value in self.data_o:
            return True
        return False
    #-------------------------------------------------------
    def passwordValidation(self, email, password):
    #-------------------------------------------------------
        if email in self.data_o:
            if password == self.data_o[email][0]:
                return True
        return False
# EOF