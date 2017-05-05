import urllib2
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

########################################################################
class HBoxWidget(Widget):
    pass

class HBoxWidget2(Widget):
    pass
########################################################################
class VBoxWidget(Widget):
    pass

########################################################################
class outNowDashApp(App):
    req = urllib2.Request("https://emoncms.org/feed/value.json?id=149796&apikey=2abd3073e21f9af1a566544f64ceb7b9")
    req2 = urllib2.Request("https://fnpyq47dr5.execute-api.eu-west-1.amazonaws.com/prod/met-barnack-obs")
    response = urllib2.urlopen(req)
    responseWittering = urllib2.urlopen(req2)
    obj = json.loads(response.read())
    objWittering = json.loads(responseWittering.read())
    windSpeedKnots = float(objWittering['windSpeed']) * float(1.15)
    print(objWittering)

    giphyQuery = "canoe"
    giphyreq = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="+giphyQuery
    giphyresponse = urllib2.urlopen(giphyreq)
    giphyObj = json.loads(giphyresponse.read())
    giphySrc = giphyObj['data']['image_url']
    print(giphySrc)

    """"""

    #----------------------------------------------------------------------
    def build(self):
        """"""
        return VBoxWidget()

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = outNowDashApp()
    app.run()
