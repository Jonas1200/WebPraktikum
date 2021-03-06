# coding: utf-8

# sehr einfache Erzeugung des Markups für vollständige Seiten
# jeweils 3 Abschnitte:
# - begin
# - content
# - end

# bei der Liste wird der content-Abschnitt wiederholt
# beim Formular nicht

import codecs
import os.path
import string

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        pass

    #-------------------------------------------------------
    def createListAbsolvent_px(self, data_opl, user):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        
        markup_s = ''
        markup_s += self.readFile_p('list0.tpl')
        markupV_s = self.readFile_p('list1Absolvent.tpl')
        lineT_o = string.Template(markupV_s)
        # mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen
        for loop_i in data_opl:
            markup_s += lineT_o.safe_substitute (absolventenfeier_s=loop_i # HIER müssen Sie eine Ergänzung vornehmen
            , begin_s=data_opl[loop_i][0]
            , end_s=data_opl[loop_i][1]
            , beschreibung_s=data_opl[loop_i][2]
            , user_s=user
            )

        markup_s += self.readFile_p('list2.tpl')

        return markup_s
    
    #-------------------------------------------------------
    def createListFB_px(self, data_opl, user):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        
        markup_s = ''
        markup_s += self.readFile_p('list0.tpl')
        markupV_s = self.readFile_p('list1FB.tpl')
        lineT_o = string.Template(markupV_s)
        # mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen
        for loop_i in data_opl:
            markup_s += lineT_o.safe_substitute (absolventenfeier_s=loop_i # HIER müssen Sie eine Ergänzung vornehmen
            , begin_s=data_opl[loop_i][0]
            , end_s=data_opl[loop_i][1]
            , beschreibung_s=data_opl[loop_i][2]
            , user_s=user
            )

        markup_s += self.readFile_p('list2.tpl')

        return markup_s
        
    #-------------------------------------------------------
    def createEditAbsolvent_px(self, data_opl, user):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        
        markup_s = ''
        markupV_s = self.readFile_p('editAbsolvent.tpl')
        lineT_o = string.Template(markupV_s)
        # mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen
        if user in data_opl:
            markup_s += lineT_o.safe_substitute (user_s=user # HIER müssen Sie eine Ergänzung vornehmen
            , name_s=data_opl[user][1]
            , firstname_s=data_opl[user][2]
            , matNr_s=data_opl[user][3]
            , company_s=data_opl[user][4]
            , theme_s=data_opl[user][5]
            , type_s=data_opl[user][6]
            )

        return markup_s
    
    #-------------------------------------------------------
    def createEditFB_px(self, data_opl, user):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        
        markup_s = ''
        markupV_s = self.readFile_p('editFB.tpl')
        lineT_o = string.Template(markupV_s)
        # mehrfach nutzen, um die einzelnen Zeilen der Tabelle zu erzeugen
        if user in data_opl:
            markup_s += lineT_o.safe_substitute (user_s=user # HIER müssen Sie eine Ergänzung vornehmen
            , name_s=data_opl[user][0]
            , firstname_s=data_opl[user][1]
            , degree_s=data_opl[user][2]
            )

        return markup_s    
    
    #-------------------------------------------------------
    def createIndex_px(self):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('home0.tpl')
        markup_s += self.readFile_p('home1.tpl')
        markup_s += self.readFile_p('home2.tpl')

        return markup_s
    #-------------------------------------------------------
    def createLoginAbsolvent_px(self):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('login0.tpl')
        markup_s += self.readFile_p('login1Absolvent.tpl')
        markup_s += self.readFile_p('login3.tpl')
        
        return markup_s

    #-------------------------------------------------------
    def createRegisterAbsolvent_px(self):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('login0.tpl')
        markup_s += self.readFile_p('login1Absolvent.tpl')
        markup_s += self.readFile_p('login2.tpl')
        markup_s += self.readFile_p('login2Absolvent.tpl')
        markup_s += self.readFile_p('login3.tpl')
        
        return markup_s
    
    #-------------------------------------------------------
    def createLoginFB_px(self):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('login0.tpl')
        markup_s += self.readFile_p('login1FB.tpl')
        markup_s += self.readFile_p('login3.tpl')
        
        return markup_s

    #-------------------------------------------------------
    def createRegisterFB_px(self):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('login0.tpl')
        markup_s += self.readFile_p('login1FB.tpl')
        markup_s += self.readFile_p('login2.tpl')
        markup_s += self.readFile_p('login2FB.tpl')
        markup_s += self.readFile_p('login3.tpl')
        
        return markup_s

    #-------------------------------------------------------
    def createAbsolventenfeier_px(self):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('Absolventenfeier.tpl')
        
        return markup_s
    
    #-------------------------------------------------------
    def createForm_px(self, id_spl, data_opl):
    #-------------------------------------------------------

        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('form0.tpl')

        markupV_s = self.readFile_p('form1.tpl')
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute (name1_s=data_opl[0] # HIER müssen Sie eine Ergänzung vornehmen
        , vorname1_s=data_opl[1]
        , matrnr1_s=data_opl[2]
        , semestAnzahl1_s=data_opl[3]
        , name2_s=data_opl[4]
        , vorname2_s=data_opl[5]
        , matrnr2_s=data_opl[6]
        , semestAnzahl2_s=data_opl[7]
        , id_s=id_spl
        )

        markup_s += self.readFile_p('form2.tpl')

        return markup_s
    #-------------------------------------------------------
    def createFormat_px(self, id_spl, data_opl):
    #-------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        markup_s = ''
        markup_s += self.readFile_p('form0.tpl')

        markupV_s = self.readFile_p('form1.tpl')
        lineT_o = string.Template(markupV_s)
        markup_s += lineT_o.safe_substitute (name1_s=data_opl[0] # HIER müssen Sie eine Ergänzung vornehmen
        , vorname1_s=data_opl[1]
        , matrnr1_s=data_opl[2]
        , semestAnzahl1_s=data_opl[3]
        , name2_s=data_opl[4]
        , vorname2_s=data_opl[5]
        , matrnr2_s=data_opl[6]
        , semestAnzahl2_s=data_opl[7]
        , id_s=id_spl
        )

        markup_s += self.readFile_p('form2.tpl')

        return markup_s
    #-------------------------------------------------------
    def readFile_p(self, fileName_spl):
    #-------------------------------------------------------
        content_s = ''
        with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()

        return content_s
# EOF