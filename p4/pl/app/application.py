# coding: utf-8

# Demonstrator / keine Fehlerbehandlung

import cherrypy

from .database import Database
from .view import View

# Method-Dispatching!

# Übersicht Anforderungen / Methoden

"""

Anforderung   GET
-------------------------
/   Liste
   liefern

/{id}   Detail
   mit {id}
   liefern
"""

class Application_cl(object):

   exposed = True # gilt für alle Methoden
   def __init__(self):
   # spezielle Initialisierung können hier eingetragen werden
      self.db_o = Database("Pension", 13)
      self.view_o = View()

   def GET(self, id=None):
      retVal_s = ''
      if id == None:
      # Anforderung der Liste
         retVal_s = self.getList_p()
      else:
      # Anforderung eines Details
         retVal_s = self.getDetail_p(id)

      return retVal_s

   def getList_p(self):
      data_a = self.db_o.read_px()
      # default-Werte entfernen
      ndata_a = data_a[1:]
      return self.view_o.createList(ndata_a)

   def getDetail_p(self, id_spl):
      data_o = self.db_o.read_px(id_spl)
      return self.view_o.createDetail(data_o)
# EOF
