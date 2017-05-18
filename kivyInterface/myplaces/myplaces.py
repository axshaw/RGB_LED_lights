# configuration
#from kivy.config import Config
#Config.set('graphics', 'width',  800)
#Config.set('graphics', 'height', 480)

import sys
from kivy.base import runTouchApp
from kivy.lang import Builder
# 52.629316, -0.407777
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from kivy.garden.mapview import MapView

root = Builder.load_string("""
#:import sys sys
#:import MapSource mapview.MapSource

<Toolbar@BoxLayout>:
    size_hint_y: None
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'
    canvas:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

<ShadedLabel@Label>:
    size: self.texture_size
    canvas.before:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

RelativeLayout:

    MapView:
        id: mapview
        lat: 52.629316
        lon: -0.407777
        zoom: 1
        map_source: MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"
        MapMarkerPopup:
            lat: 52.629316
            lon: -0.407777
            popup_size: dp(230), dp(130)
            Bubble:
                BoxLayout:
                    orientation: "horizontal"
                    padding: "5dp"
                    #AsyncImage:
                    #    source: "./zac.jpg"
                    #    mipmap: True
                    Label:
                        text: "[b]Barnack[/b]\\nHome \\nMission Control"
                        markup: True
                        halign: "center"
        MapMarkerPopup:
            lat: 38.110590
            lon: 20.813998
            popup_size: dp(230), dp(130)
            Bubble:
                BoxLayout:
                    orientation: "horizontal"
                    padding: "5dp"
                    #AsyncImage:
                    #    source: "http://upload.wikimedia.org/wikipedia/commons/9/9d/France-Lille-VieilleBourse-FacadeGrandPlace.jpg"
                    #    mipmap: True
                    Label:
                        text: "[b]Skala[/b]\\nLittle Blue House"
                        markup: True
                        halign: "center"
        MapMarkerPopup:
            lat: 48.787341
            lon: -3.450037
            popup_size: dp(230), dp(130)
            Bubble:
                BoxLayout:
                    orientation: "horizontal"
                    padding: "5dp"
                    #AsyncImage:
                    #    source: "http://upload.wikimedia.org/wikipedia/commons/9/9d/France-Lille-VieilleBourse-FacadeGrandPlace.jpg"
                    #    mipmap: True
                    Label:
                        text: "[b]Perros Guirec[/b]\\nLittle Yellow\\nHouse"
                        markup: True
                        halign: "center"
    Toolbar:
        top: root.top
        Button:
            text: "Move to Barnack, UK"
            on_release: mapview.center_on(52.629316, -0.407777)
        Button:
            text: "Move to Sydney, Autralia"
            on_release: mapview.center_on(-33.867, 151.206)
        Button:
            text: "Return to World"
            on_release: mapview.center_on(0, 0)
        Spinner:
            text: "mapnik"
            values: MapSource.providers.keys()
            on_text: mapview.map_source = self.text
    Toolbar:
        Label:
            text: "Longitude: {}".format(mapview.lon)
        Label:
            text: "Latitude: {}".format(mapview.lat)
""")

runTouchApp(root)
