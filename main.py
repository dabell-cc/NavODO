from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class TestScreen(Widget):
    pass

class NavODOApp(App):
    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    NavODOApp().run()
