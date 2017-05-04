import urllib2
import json

from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        req = urllib2.Request("http://api.open-notify.org/iss-now.json")
        response = urllib2.urlopen(req)

        obj = json.loads(response.read())
        print(obj)
        print(obj['iss_position']['latitude'])
        latPos = obj['iss_position']['latitude']
        lonPos = obj['iss_position']['longitude']
        mapview = MapView(zoom=5, lat=obj['iss_position']['latitude'], lon=obj['iss_position']['longitude'])
        return mapview

MapViewApp().run()
