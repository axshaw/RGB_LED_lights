# configuration
from kivy.config import Config
Config.set('graphics', 'width',  800)
Config.set('graphics', 'height', 480)

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
MapView:
    lat: 0
    lon: 0
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
                AsyncImage:
                    source: "http://upload.wikimedia.org/wikipedia/commons/9/9d/France-Lille-VieilleBourse-FacadeGrandPlace.jpg"
                    mipmap: True
                Label:
                    text: "[b]Lille[/b]\\n1 154 861 hab\\n5 759 hab./km2"
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
                AsyncImage:
                    source: "http://upload.wikimedia.org/wikipedia/commons/9/9d/France-Lille-VieilleBourse-FacadeGrandPlace.jpg"
                    mipmap: True
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
                AsyncImage:
                    source: "http://upload.wikimedia.org/wikipedia/commons/9/9d/France-Lille-VieilleBourse-FacadeGrandPlace.jpg"
                    mipmap: True
                Label:
                    text: "[b]Perros Guirec[/b]\\nLittle Yellow\\nHouse"
                    markup: True
                    halign: "center"
""")

runTouchApp(root)
