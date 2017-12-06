# coding: utf-8

import cherrypy
import collections

from .database import Database_cl
from .view import View_cl

#-----------------------------------------------------------
class Application_cl(object):
#-----------------------------------------------------------

    #-------------------------------------------------------
    def __init__(self):
    #-------------------------------------------------------
        # spezielle Initialisierung können hier eingetragen werden
        #self.db_o = Database_cl('webteams.json',4)
        self.absolventenfeier_o = Database_cl('Absolventenfeier.json',5)
        self.absolvent_o = Database_cl('Absolvent.json',8)
        self.fb_o = Database_cl('FB.json',6)
        self.anmeldungen_absolvent_o = Database_cl('AbsolventAnmeldung.json',2)
        self.anmeldungen_fb_o = Database_cl('FBAnmeldung.json',6)
        self.absolvent_prüfer = Database_cl('AbsolventPrüfer.json', 3)
        self.view_o = View_cl("C:\\Users\\jks\\sciebo\\5.Semester\\WEB\\Praktikum\\web\\p3\\Absolventenfeier")

    @cherrypy.expose
    #-------------------------------------------------------
    def index(self):
    #-------------------------------------------------------
        return self.createIndex_p()

    @cherrypy.expose
    # -------------------------------------------------------
    def eval(self):
        # -------------------------------------------------------
        return self.evaluation_p()

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
    def TeilnahmeListe(self, data):
    #-------------------------------------------------------
        Absolventenfeier = self.absolventenfeier_o.read_px(data)
        anmeldungen = self.anmeldungen_absolvent_o.getIdList(data, 1)
        if len(anmeldungen) == 0:
            raise cherrypy.HTTPRedirect("/eval")
        angemeldeteAbsolventen = []
        for loop in anmeldungen:
            angemeldeteAbsolventen.append(self.anmeldungen_absolvent_o.data_o[loop][0])
        TeilnehmerDict = {}
        for loop in angemeldeteAbsolventen:
            Absolvent = self.absolvent_o.read_px(loop)
            TeilnehmerDict[Absolvent[2]] = Absolvent[5]
        #orderedDict = collections.OrderedDict(sorted(TeilnehmerDict.items()))
        i = 0
        finishedDict = {}
        for loop in sorted(TeilnehmerDict):
            finishedDict[i] = [loop,TeilnehmerDict[loop]]
            i += 1
        fasd = finishedDict[0]
        return self.view_o.createList_px('TeilnahmeListe.tpl', finishedDict,Absolventenfeier[0])


    @cherrypy.expose
    #-------------------------------------------------------
    def applyAbsolvent(self, **data):
    #-------------------------------------------------------
        data_a = [ data['user']
                  ,data['absolventenfeier']
        ]
        if not self.anmeldungen_absolvent_o.entryExists_px(data['user']):
            self.anmeldungen_absolvent_o.create_px(data_a)
        raise cherrypy.HTTPRedirect("/index")
    
    @cherrypy.expose
    #-------------------------------------------------------
    def applyFB(self, **data):
    #-------------------------------------------------------
        data_a = [ data['user']
                  ,data['absolventenfeier']
        ]
        if not self.anmeldungen_fb_o.entryExists_px(data['user']):
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
    def deleteAbsolventenfeier(self, data):
    #-------------------------------------------------------
        anmeldungen = self.anmeldungen_absolvent_o.getIdList(data, 1)
        for loop in anmeldungen:
            self.anmeldungen_absolvent_o.delete_px(loop)
        self.absolventenfeier_o.delete_px(data)
        raise cherrypy.HTTPRedirect("/eval")

    @cherrypy.expose
    #-------------------------------------------------------
    def editAbsolventenfeier(self, data):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = [data] + self.absolventenfeier_o.read_px(data)
        return self.view_o.createList_px('updateAbsolventenfeier.tpl', data_a)

    @cherrypy.expose
    #-------------------------------------------------------
    def editAbsolvent(self, data):
    #-------------------------------------------------------
        data_a = self.absolvent_o.read_px()
        return self.view_o.createEditAbsolvent_px(data_a, self.absolvent_o.getEntryID(data))

    @cherrypy.expose
    #-------------------------------------------------------
    def editFB(self, data):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = self.fb_o.read_px()
        return self.view_o.createEditFB_px(data_a, self.fb_o.getEntryID(data))

    @cherrypy.expose
    #-------------------------------------------------------
    def AbsolventenListe(self):
    #-------------------------------------------------------
        data_o = self.absolvent_o.read_px()
        return self.view_o.createList_px('AbsolventenListe.tpl',data_o)

    @cherrypy.expose
    # -------------------------------------------------------
    def PrüferZuordnen(self, data):
        # -------------------------------------------------------
        zugeordnet = self.absolvent_prüfer.getIdList(data, 0)
        vars = []
        if len(zugeordnet) != 0:
            vars = self.absolvent_prüfer.read_px(zugeordnet)
        else:
            vars = [' ',' ']
        vars += self.absolvent_o.read_px(data)
        data_o = self.fb_o.read_px()
        fb_prof_ids = self.fb_o.getIdList("Professor",6)
        data_b = {}
        for loop in fb_prof_ids:
            if int(loop) != 0:
                data_b[str(loop)] = self.fb_o.read_px(loop)
        return self.view_o.createList_px('PrüferZuordnen.tpl', data_o, vars, data_b)

    @cherrypy.expose
    # -------------------------------------------------------
    def updateAbsolventenfeier(self, **data_opl):
        # -------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = [data_opl["id_s"]
            , data_opl["absolventenfeier_s"]
            , data_opl["begin_t"]
            , data_opl["end_t"]
            , data_opl["beschreibung_s"]
            ]
        self.absolventenfeier_o.update_px(data_a)
        return self.evaluation_p()

    @cherrypy.expose
    #-------------------------------------------------------
    def confirmEditAbsolvent(self, **data_opl):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = [ data_opl["id_s"]
                  ,data_opl["user_s"]
                  ,data_opl["name_s"]
                  ,data_opl["firstname_s"]
                  ,data_opl["matNr_s"]
                  ,data_opl["company_s"]
                  ,data_opl["theme_s"]
                  ,data_opl["type_s"]
        ]
        self.absolvent_o.update_px(data_a)        
        return self.createListAbsolvent_p(data_opl["id_s"])
     
    @cherrypy.expose
    #-------------------------------------------------------
    def confirmEditFB(self, **data_opl):
    #-------------------------------------------------------
        # Eintrag löschen, dann Liste neu anzeigen
        data_a = [ data_opl["id_s"]
                  ,data_opl["user_s"]
                  ,data_opl["name_s"]
                  ,data_opl["firstname_s"]
                  ,data_opl["degree_s"]
        ]      
        self.fb_o.updateFB_px(data_a)        
        return self.createListFB_p(data_opl["id_s"])

    @cherrypy.expose
    #-------------------------------------------------------
    def submitLoginAbsolvent(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!

        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        if len(data_opl) == 2:
            if not self.absolvent_o.passwordValidation(data_opl["user_s"],data_opl["password_s"]):
                raise cherrypy.HTTPRedirect("/loginAbsolvent")
                #error handling falls javascript deaktiviert ist
            else:
                return self.createListAbsolvent_p(self.absolvent_o.getEntryID(data_opl["user_s"]))
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
            else:
                raise cherrypy.HTTPRedirect("/addAbsolvent")
        return self.createListAbsolvent_p(self.absolvent_o.getEntryID(data_opl["user_s"]))
    @cherrypy.expose
    #-------------------------------------------------------
    def submitLoginFB(self, **data_opl):
    #-------------------------------------------------------
        # Sichern der Daten: aufgrund der Formularbearbeitung muss
        # eine vollständige HTML-Seite zurückgeliefert werden!

        # data_opl: Dictionary mit den gelieferten key-value-Paaren
        if len(data_opl) == 2:
            if not self.fb_o.passwordValidation(data_opl["user_s"],data_opl["password_s"]):
                raise cherrypy.HTTPRedirect("/loginFB")
            else:
                return self.createListFB_p(self.fb_o.getEntryID(data_opl["user_s"]))
        if len(data_opl) >= 3:
            if not self.fb_o.entryExists_px(data_opl["user_s"]):
                data_a = [ data_opl["user_s"]
                          ,data_opl["password_s"]
                          ,data_opl["name_s"]
                          ,data_opl["firstname_s"]
                          ,data_opl["degree_s"]
                          ,data_opl["inspector_s"]
                          ,data_opl["type_s"]
                ]
                self.fb_o.create_px(data_a)
        
        return self.createListFB_p(data_opl["user_s"])
    
    @cherrypy.expose
    #-------------------------------------------------------
    def submitAbsolventenfeier(self, **data_opl):
    #-------------------------------------------------------
        data_a = [ data_opl["absolventenfeier_s"]
                  ,data_opl["begin_t"]
                  ,data_opl["end_t"]
                  ,data_opl["beschreibung_s"]
        ]
        self.absolventenfeier_o.create_px(data_a)
        raise cherrypy.HTTPRedirect("/eval")

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
    #-------------------------------------------------------
    def evaluation_p(self):
    #-------------------------------------------------------
        data_o = self.absolventenfeier_o.read_px()
        return self.view_o.createList_px('eval.tpl', data_o)
# EOF