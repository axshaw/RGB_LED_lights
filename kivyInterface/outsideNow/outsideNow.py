import urllib2
import json
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
# https://fnpyq47dr5.execute-api.eu-west-1.amazonaws.com/prod/met-barnack-obs
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        req = urllib2.Request("https://emoncms.org/feed/value.json?id=149796&apikey=2abd3073e21f9af1a566544f64ceb7b9")
        req2 = urllib2.Request("https://fnpyq47dr5.execute-api.eu-west-1.amazonaws.com/prod/met-barnack-obs")
        response = urllib2.urlopen(req)
        responseWittering = urllib2.urlopen(req2)
        obj = json.loads(response.read())
        objWittering = json.loads(responseWittering.read())
        print(obj)
        print(objWittering)
        print('---------------------------------------------------------------------')
        return Label(text=obj)


if __name__ == '__main__':
    MyApp().run()
