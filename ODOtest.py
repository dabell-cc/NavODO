from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.clock import Clock
import obd  
from obd import OBDCommand

class ODOScreen(Widget):
    service_km = NumericProperty(380.8)
    curr_kph = NumericProperty(75)
    curr_rpm = NumericProperty(3600)
    connection = None

    def connect(self):
        self.connection = obd.OBD()
    

    def update(self, dt):
        self.service_km = self.connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR)
        self.curr_kph = self.connection.query(obd.commands.SPEED)
        self.curr_rpm = self.connection.query(obd.commands.RPM)


class ODOTestApp(App):
    def build(self):
        odo = ODOScreen()
        odo.connect()
        Clock.schedule_interval(odo.update, 1.0/2.0)
        return

if __name__ == '__main__':
    ODOTestApp().run()