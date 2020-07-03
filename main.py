import kivy
import time
kivy.require('1.11.1')

import sys, os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config 
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.graphics import Canvas
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy_deps import sdl2, glew
import pkg_resources.py2_warn
import pkg_resources

Config.set('graphics', 'width', 1240)
Config.set('graphics', 'height', 640)
Config.set('graphics', 'resizable', False)

def resourcePath():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)
    return os.path.join(os.path.abspath("."))

def resource_path(relative_path):
    try:
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Main(BoxLayout):
    def __init__(self):
        super(Main, self).__init__() 
        self.layouts = [] 
        self.i = 0      
        self.CT = Container()
        self.add_widget(self.CT)
        self.layouts.append(self.CT.MN)
        self.layouts.append(self.CT.Mod)
        self.layouts.append(self.CT.Dom)
        self.layouts.append(self.CT.Con)
        self.layouts.append(self.CT.Mall)
        self.layouts.append(self.CT.Tab)
        self.layouts.append(self.CT.Mef)
        self.layouts.append(self.CT.Ens)
        self.layouts.append(self.CT.Des)

    def showModelo(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Mod)
        self.i = 1

    def showDominio(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Dom)
        self.i = 2
    
    def showCondiciones(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Con)
        self.i = 3
    
    def showMalla(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Mall)
        self.i = 4

    def showTabla(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Tab)
        self.i = 5
    
    def showMef(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Mef)
        self.i = 6

    def showEnsamblaje(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Ens)
        self.i = 7
    
    def showDespedida(self, *arg):
        self.CT.remove_widget(self.layouts[self.i])
        self.CT.add_widget(self.CT.Des)
        self.i = 8

class Container(BoxLayout):
    def __init__(self):
        super(Container, self).__init__()
        self.MN = ImageMain()
        self.add_widget(self.MN)
        self.Mod = Modelo()
        self.Dom = Dominio()
        self.Con = Condiciones()
        self.Mall = Malla()
        self.Tab = Tabla()
        self.Mef = Mef()
        self.Ens = Ensamblaje()
        self.Des = Despedida()

class ImageMain(BoxLayout):
    None

class Modelo(BoxLayout):
    def __init__(self):
        super(Modelo, self).__init__()

class Dominio(BoxLayout):
    def __init__(self):
        super(Dominio, self).__init__()
        self.i = 1
        self.MG = AsyncImage(size_hint=(1,10), source=resource_path('img/Dominio' + str(self.i) + '.png'))
        self.add_widget(self.MG)
    
    def anterior(self, *arg):
        if(self.i != 1):
            self.i -= 1
            self.MG.source=resource_path('img/Dominio' + str(self.i) + '.png')

    def siguiente(self, *arg):
        if(self.i != 4):
            self.i += 1
            self.MG.source=resource_path('img/Dominio' + str(self.i) + '.png')

class Condiciones(BoxLayout):
    def __init__(self):
        super(Condiciones, self).__init__()
        self.flag = 1
        self.DI = AsyncImage(size_hint=(1,10), source=resource_path('img/Dirichlet.png'))
        self.NE = AsyncImage(size_hint=(1,10), source=resource_path('img/Neumann.png'))
        self.add_widget(self.DI)
    
    def dirich(self, *arg):
        if(self.flag != 1):
            self.remove_widget(self.NE)
            self.add_widget(self.DI)
            self.flag = 1
    
    def neum(self, *arg):
        if(self.flag != 2):
            self.remove_widget(self.DI)
            self.add_widget(self.NE)
            self.flag = 2


class Malla(BoxLayout):
    def __init__(self):
        super(Malla, self).__init__()
        self.i = 1
        self.MG = AsyncImage(size_hint=(1,10), source=resource_path('img/Malla' + str(self.i) + '.png'))
        self.add_widget(self.MG)
    
    def anterior(self, *arg):
        if(self.i != 1):
            self.i -= 1
            self.MG.source=resource_path('img/Malla' + str(self.i) + '.png')

    def siguiente(self, *arg):
        if(self.i != 4):
            self.i += 1
            self.MG.source=resource_path('img/Malla' + str(self.i) + '.png')
    
class Tabla(BoxLayout):
    def __init__(self):
        super(Tabla, self).__init__()

class Mef(BoxLayout):
    def __init__(self):
        super(Mef, self).__init__()
        self.orientation = 'vertical'
        self.i = 1
        self.MG = AsyncImage(size_hint=(1,10), source=resource_path('img/MefScreen' + str(self.i) + '.png'))
        self.add_widget(self.MG)
    
    def anterior(self, *arg):
        if(self.i != 1):
            self.i -= 1
            self.MG.source=resource_path('img/MefScreen' + str(self.i) + '.png')
    
    def siguiente(self, *arg):
        if(self.i != 18):
            self.i += 1
            self.MG.source=resource_path('img/MefScreen' + str(self.i) + '.png')

class Ensamblaje(BoxLayout):
    def __init__(self):
        super(Ensamblaje, self).__init__()
        self.i = 1
        self.MG = AsyncImage(size_hint=(1,10), source=resource_path('img/Ensamblaje' + str(self.i) + '.png'))
        self.add_widget(self.MG)

    def anterior(self, *arg):
        if(self.i != 1):
            self.i -= 1
            self.MG.source=resource_path('img/Ensamblaje' + str(self.i) + '.png')
    
    def siguiente(self, *arg):
        if(self.i != 7):
            self.i += 1
            self.MG.source=resource_path('img/Ensamblaje' + str(self.i) + '.png')

class Despedida(BoxLayout):
    def __init__(self):
        super(Despedida, self).__init__()

class MainApp(App):
    title = "00170517"
    def build(self):
        return Main()

if __name__=='__main__':
    kivy.resources.resource_add_path(resourcePath())
    MainApp().run()
