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
        self.absolventenfeier_o = Database_cl('Absolventenfeier.json',4)
        self.absolvent_o = Database_cl('Absolvent.json',7)
        self.fb_o = Database_cl('FB.json',5)
        self.anmeldungen_absolvent_o = Database_cl('AbsolventAnmeldung.json',5)
        self.anmeldungen_fb_o = Database_cl('FBAnmeldung.json',5)
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
    def addAbsolventenfeier(self):
    #-------------------------------------------------------
        return self.createAbsolventenfeier_p()

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
    def applyAbsolvent(self, data):
    #-------------------------------------------------------
        data_a = [ self.getUser(data)
                  ,self.getAbsolventenfeier(data)
        ]
        self.anmeldungen_absolvent_o.create_px(data_a)
        raise cherrypy.HTTPRedirect("/index") 
    
    @cherrypy.expose
    #-------------------------------------------------------
    def applyFB(self, data):
    #-------------------------------------------------------
        data_a = [ self.getUser(data)
                       ,self.getAbsolventenfeier(data)
        ]        
        self.anmeldungen_fb_o.create_px(data_a)
        raise cherrypy.HTTPRedirect("/index")
    
    @cherrypy.expose
    #-------------------------------------------------------
    def deleteSignInAbsolvent(self, data):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen

        self.anmeldungen_absolvent_o.delete_px(data)
        raise cherrypy.HTTPRedirect("/index")
    
    @cherrypy.expose
    #-------------------------------------------------------
    def deleteSignInFB(self, data):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen

        self.anmeldungen_fb_o.delete_px(data)
        raise cherrypy.HTTPRedirect("/index")
    
    @cherrypy.expose
    #-------------------------------------------------------
    def editAbsolvent(self, data):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = self.absolvent_o.read_px()
        return self.view_o.createEditAbsolvent_px(data_a, data)
     
    @cherrypy.expose
    #-------------------------------------------------------
    def editFB(self, data):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = self.fb_o.read_px()
        return self.view_o.createEditFB_px(data_a, data)
          
    @cherrypy.expose
    #-------------------------------------------------------
    def confirmEditAbsolvent(self, **data_opl):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = [ data_opl["user_s"]
                  ,data_opl["name_s"]
                  ,data_opl["firstname_s"]
                  ,data_opl["matNr_s"]
                  ,data_opl["company_s"]
                  ,data_opl["theme_s"]
                  ,data_opl["type_s"]
        ]
        self.absolvent_o.update_px(data_a)        
        return self.createListAbsolvent_p(data_opl["user_s"])
     
    @cherrypy.expose
    #-------------------------------------------------------
    def confirmEditFB(self, **data_opl):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = [ data_opl["user_s"]
                  ,data_opl["name_s"]
                  ,data_opl["firstname_s"]
                  ,data_opl["degree_s"]
        ]      
        self.fb_o.updateFB_px(data_a)        
        return self.createListFB_p(data_opl["user_s"])
    
    #-------------------------------------------------------
    def getUser(self, data):
    #-------------------------------------------------------
        return data[:-(len(self.getAbsolventenfeier(data))+1)]
    
    #-------------------------------------------------------
    def getAbsolventenfeier(self, data):
    #-------------------------------------------------------
        pos = data.index('&')+1
        return data[pos:]  
    
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
            if not self.absolvent_o.entryExists_px(data_opl["user_s"]):
                raise cherrypy.HTTPRedirect("/addAbsolvent")
            else:
                if not self.absolvent_o.passwordValidation(data_opl["user_s"],data_opl["password_s"]):
                    test = 3 #löschen
                    #error handling falls javascript deaktiviert ist
                    
        if len(data_opl) >= 3:
            if not self.absolvent_o.entryExists_px(data_opl["user_s"]):
                data_a = [ data_opl["user_s"]
                          ,data_opl["password_s"]
                          ,data_opl["name_s"]
                          ,data_opl["firstname_s"]
                          ,data_opl["matNr_s"]
                          ,data_opl["company_s"]
                          ,data_opl["theme_s"]
                          ,data_opl["type_s"]
                ]
                self.absolvent_o.create_px(data_a)
        
        return self.createListAbsolvent_p(data_opl["user_s"])
    @cherrypy.expose
    #-------------------------------------------------------
    def submitLoginFB(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!

        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        if len(data_opl) == 2:
            if not self.fb_o.entryExists_px(data_opl["user_s"]):
                raise cherrypy.HTTPRedirect("/addFB")
            else:
                if not self.fb_o.passwordValidation(data_opl["user_s"],data_opl["password_s"]):
                    test = 3 #löschen
                    #error handling
                    
        if len(data_opl) >= 3:
            if not self.fb_o.entryExists_px(data_opl["user_s"]):
                data_a = [ data_opl["user_s"]
                          ,data_opl["password_s"]
                          ,data_opl["name_s"]
                          ,data_opl["firstname_s"]
                          ,data_opl["degree_s"]
                          ,data_opl["inspector_s"]
                ]
                self.fb_o.create_px(data_a)
        
        return self.createListFB_p(data_opl["user_s"])
    
    @cherrypy.expose
    #-------------------------------------------------------
    def submitAbsolventenfeier(self, **data_opl):
    #-------------------------------------------------------
        if not self.absolventenfeier_o.entryExists_px(data_opl["absolventenfeier_s"]):
            data_a = [ data_opl["absolventenfeier_s"]
                      ,data_opl["begin_t"]
                      ,data_opl["end_t"]
                      ,data_opl["beschreibung_s"]
            ]
            self.absolventenfeier_o.create_px(data_a)
        raise cherrypy.HTTPRedirect("/index")
        #return self.createAbsolventenfeier_p()
        

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
    def createListAbsolvent_p(self, user):
    #-------------------------------------------------------
        data_o = self.absolventenfeier_o.read_px()
        # mit diesen Daten Markup erzeugen
        return self.view_o.createListAbsolvent_px(data_o, user)
    
    #-------------------------------------------------------
    def createListFB_p(self, user):
    #-------------------------------------------------------
        data_o = self.absolventenfeier_o.read_px()
        # mit diesen Daten Markup erzeugen
        return self.view_o.createListFB_px(data_o, user)
    
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
    
    #-------------------------------------------------------
    def createAbsolventenfeier_p(self):
    #-------------------------------------------------------
        return self.view_o.createAbsolventenfeier_px()     
# EOF
