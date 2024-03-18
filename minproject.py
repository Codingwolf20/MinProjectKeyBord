import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.floatlayout  import FloatLayout
from kivy.core.window import Window

class MyGridlayout(GridLayout):

    pass
class MYApplication(App):
    def build(self):
        Window.size=[800,600]    
        return MyGridlayout()
    
if __name__=="__main__":
    MYApplication().run()   