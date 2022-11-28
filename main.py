from kivy.app import App
from kivy.clock import Clock
from kivy.uix.image import Image

import requests as rq
from bs4 import BeautifulSoup as bs

img =  Image(source = 'imgs/err.jpg')
class MyApp(App):

    def on_start(self):
        Clock.schedule_interval(self.update_label, .5)

    def update_label(self, *args):
        try:
            r = rq.get("http://192.168.1.106:5000/monitors")
            data = bs(r.content, 'html.parser').select("#id")[0]['value']
            img.source = f'imgs/{data}.jpg'
        except:
            img.source = f'imgs/err.jpg'

    def build(self):
        return img

if __name__ == '__main__':
    MyApp().run()