from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class DistanceElement(Widget):
    pass

class ODOElement(Widget):
    pass

class TestElement(Widget):
    pass

class TestScreen(Widget):
    pass

class NavODOApp(App):
    def build(self):
        # return Label(text='Hello world')
        return TestScreen()


if __name__ == '__main__':
    NavODOApp().run()
