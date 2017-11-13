# coding: utf-8

import cherrypy

from .database import Database_cl
from .view import View_cl

#-----------------------------------------------------------
class Application_cl(object):
#-----------------------------------------------------------

    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_cl('webteams.json',4)
        self.absolventenfeier_o = Database_cl('Absolventenfeier.json',5)
        self.absolvent_o = Database_cl('Absolvent.json',9)
        self.fb_o = Database_cl('FB.json',6)
        self.view_o = View_cl()

    @cherrypy.expose
    #-------------------------------------------------------
    def index(self):
    #-------------------------------------------------------
        return self.createIndex_p()

    @cherrypy.expose
    #-------------------------------------------------------
    def addAbsolvent(self):
    #-------------------------------------------------------
        return self.createRegisterAbsolvent_p()

    @cherrypy.expose
    #-------------------------------------------------------
    def addFB(self):
    #-------------------------------------------------------
        return self.createRegisterFB_p()

    @cherrypy.expose
    #-------------------------------------------------------
    def loginAbsolvent(self):
    #-------------------------------------------------------
        return self.createLoginAbsolvent_p()
    
    @cherrypy.expose
    #-------------------------------------------------------
    def loginFB(self):
    #-------------------------------------------------------
        return self.createLoginFB_p()
    
    @cherrypy.expose
    #-------------------------------------------------------
    def save(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!

        # data_opl: Dictionary mit den gelieferten key-value-Paaren

        # hier müsste man prüfen, ob die Daten korrekt vorliegen!

        # HIER müssen Sie die Semesterzahl(en) ergänzen

        id_s = data_opl["id_s"]
        data_a = [ data_opl["name1_s"]
        , data_opl["vorname1_s"]
        , data_opl["matrnr1_s"]
        , data_opl["semestAnzahl1_s"]
        , data_opl["name2_s"]
        , data_opl["vorname2_s"]
        , data_opl["matrnr2_s"]
        , data_opl["semestAnzahl2_s"]
        ]
        if id_s != "None":
            # Update-Operation
            self.db_o.update_px(id_s, data_a)
        else:
            # Create-Operation
            id_s = self.db_o.create_px(data_a)
        
        return self.createForm_p(id_s)

    @cherrypy.expose
    #-------------------------------------------------------
    def submitLoginAbsolvent(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!

        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        if len(data_opl) == 2:
            if self.absolvent_o.userExists_px(data_opl["user_s"]):
                data_a = [ data_opl["user_s"]
                           ,data_opl["password_s"]
                ]
                
        if len(data_opl) == 3:
            if self.absolvent_o.userExists_px(data_opl["user_s"]):
                data_a = [ data_opl["user_s"]
                          ,data_opl["password_s"]
                          ,data_opl["password2_s"]
                ]
        if id_s != "None":
            # Update-Operation
            self.db_o.update_px(id_s, data_a)
        else:
            # Create-Operation
            id_s = self.db_o.create_px(data_a)
        
        return self.createForm_p(id_s)

    @cherrypy.expose
    #-------------------------------------------------------
    def delete(self, id):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen

        self.db_o.delete_px(id)
        return self.createList_p()

    @cherrypy.expose
    #-------------------------------------------------------
    def default(self, *arguments, **kwargs):
    #-------------------------------------------------------
        msg_s = "unbekannte Anforderung: " + \
                str(arguments) + \
                ' ' + \
                str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
    default.exposed= True

    #-------------------------------------------------------
    def createList_p(self):
    #-------------------------------------------------------
        data_o = self.db_o.read_px()
        # mit diesen Daten Markup erzeugen
        return self.view_o.createList_px(data_o)
    #-------------------------------------------------------
    def createIndex_p(self):
    #-------------------------------------------------------
        return self.view_o.createIndex_px()
    #-------------------------------------------------------
    def createForm_p(self, id_spl = None):
    #-------------------------------------------------------
        if id_spl != None:
            data_o = self.db_o.read_px(id_spl)
        else:
            data_o = self.db_o.getDefault_px()
        # mit diesen Daten Markup erzeugen
        return self.view_o.createForm_px(id_spl, data_o)
    #-------------------------------------------------------
    def createLoginAbsolvent_p(self):
    #-------------------------------------------------------
        return self.view_o.createLoginAbsolvent_px()
    #-------------------------------------------------------
    def createRegisterAbsolvent_p(self):
    #-------------------------------------------------------
        return self.view_o.createRegisterAbsolvent_px()
    #-------------------------------------------------------
    def createLoginFB_p(self):
    #-------------------------------------------------------
        return self.view_o.createLoginFB_px()
    #-------------------------------------------------------
    def createRegisterFB_p(self):
    #-------------------------------------------------------
        return self.view_o.createRegisterFB_px()    
    
# EOF
