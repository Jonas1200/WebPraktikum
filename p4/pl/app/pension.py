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

class Pension(object):

   exposed = True # gilt für alle Methoden
   def __init__(self):
   # spezielle Initialisierung können hier eingetragen werden
      self.db = Database("Pension", 13)
      self.view = View()

   def GET(self, id=None):
      retVal = ''
      if id == None:
      # Anforderung der Liste
         retVal = self.getList()
      else:
      # Anforderung eines Details
         retVal = self.getDetail(id)
      return retVal

   def getList(self):
      data = self.db.read()
      # default-Werte entfernen
      newdata = data[1:]
      return self.view.createList(newdata)

   def getDetail(self, id):
      data = self.db.read(id)
      return self.view.createDetail(data)
# EOF
