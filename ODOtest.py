from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.clock import Clock
import obd  
from obd import OBDCommand

class ODOScreen(Widget):
    service_km = StringProperty(380.8)
    curr_kph = StringProperty(75)
    curr_rpm = StringProperty(3600)
    connection = None

    def connect(self):
        self.connection = obd.OBD(portstr='\\.\\COM5')
        # pass

    def update(self, dt):
        self.service_km = str(self.connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR))
        self.curr_kph = str(self.connection.query(obd.commands.SPEED))
        self.curr_rpm = str(self.connection.query(obd.commands.RPM))
        # pass


class ODOTestApp(App):
    def build(self):
        odo = ODOScreen()
        odo.connect()
        Clock.schedule_interval(odo.update, 1.0/2.0)
        return odo

if __name__ == '__main__':
    ODOTestApp().run()