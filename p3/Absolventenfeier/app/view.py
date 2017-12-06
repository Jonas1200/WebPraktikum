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
from mako.template import Template
from mako.lookup import TemplateLookup

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

    #-------------------------------------------------------
    def __init__(self, path_spl):
    #-------------------------------------------------------
        self.path_s = os.path.join(path_spl, "template")
        self.lookup_o = TemplateLookup(directories=[self.path_s])
        #self.lookup_o = TemplateLookup(directories=['../template/'], module_directory='/tmp')
        pass

    # -------------------------------------------------------
    def createList_px(self, template_spl, data_opl, vars=None, data_b=None):
        # -------------------------------------------------------
        # hier müsste noch eine Fehlerbehandlung ergänzt werden !
        #template_path = os.path.join(self.path_s, template_spl)
        #template_o = Template(filename=template_path)
        template_o = self.lookup_o.get_template(template_spl)

        #markup_s = template_o.render(data_o=data_opl)
        markup_s = template_o.render(data_o = data_opl, vars=vars, data_b=data_b)
        #markup_s = ''
        return markup_s

    # -------------------------------------------------------
    def createListAbsolvent_px(self, data_opl, user):
        # -------------------------------------------------------
        markup_s = ''
        markup_s += self.readFile_p('list0.tpl')
        markupV_s = self.readFile_p('list1Absolvent.tpl')
        lineT_o = string.Template(markupV_s)
        for loop_i in data_opl:
            if int(loop_i) != 0:
                markup_s += lineT_o.safe_substitute(absolventenfeier_s=data_opl[loop_i][0]  # HIER müssen Sie eine Ergänzung vornehmen
                                                    , begin_s=data_opl[loop_i][1]
                                                    , end_s=data_opl[loop_i][2]
                                                    , beschreibung_s=data_opl[loop_i][3]
                                                    , user_s=user
                                                    , id_s=loop_i
                                                    )
        markup_s += self.readFile_p('list2.tpl')

        return markup_s

    #-------------------------------------------------------
    def createListFB_px(self, data_opl, user):
    #-------------------------------------------------------
        markup_s = ''
        markup_s += self.readFile_p('list0.tpl')
        markupV_s = self.readFile_p('list1FB.tpl')
        lineT_o = string.Template(markupV_s)
        for loop_i in data_opl:
            if int(loop_i) != 0:
                markup_s += lineT_o.safe_substitute (absolventenfeier_s=data_opl[loop_i][0] # HIER müssen Sie eine Ergänzung vornehmen
                , begin_s=data_opl[loop_i][1]
                , end_s=data_opl[loop_i][2]
                , beschreibung_s=data_opl[loop_i][3]
                , user_s=user
                , id_s=loop_i
                )

        markup_s += self.readFile_p('list2.tpl')

        return markup_s

    #-------------------------------------------------------
    def createEditAbsolvent_px(self, data_opl, user):
    #-------------------------------------------------------

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
        markup_s += self.readFile_p('home.tpl')

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
        return self.readFile_p('Absolventenfeier.html')

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