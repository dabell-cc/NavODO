# Kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,StringProperty, \
    BooleanProperty, ObjectProperty
from kivy.clock import Clock
import sys

# Time
import time
from time import monotonic as timer
from datetime import timedelta 

# OBD
import obd
from obd import OBDCommand

# Misc
import decimal


class TestScreen(Widget):
    # Timing and Clock
    clock_timeofday = StringProperty()
    stopwatch_disp = StringProperty('')
    stopwatch_dt = 0
    stopwatch_start = 0
    stopwatch_stop = 0
    stopwatch_is_running = BooleanProperty(False)

    speed_time_new = None
    speed_time_old = None

    # OBD globals
    connection = None

    # Speeds
    speed_CAS = NumericProperty(0)
    speed_Curr = NumericProperty(0)

    # Distances
    distance_incODO = NumericProperty(0)
    distance_stageODO = NumericProperty(0)
    reverse_label = StringProperty('Forward')
    reverse_flag = False

    locked = False

    def test_callback(self):
        print('button push')

    def unlock(self):
        # self.locked = False
        pass
    
    def lock(self):
        # self.locked = True
        pass

    def reverse_toggle(self):
        if(not self.locked):
            self.reverse_flag = not self.reverse_flag
            if(self.reverse_flag):
                self.reverse_label = 'Reverse'
            else:
                self.reverse_label = 'Forward'

    def zero_CAS(self):
        if(not self.locked):
            self.speed_CAS = self.speed_Curr
    
    def zero_stageODO(self):
        if(not self.locked):
            self.distance_stageODO = 0
            self.distance_incODO = 0
    
    def zero_incODO(self):
        if(not self.locked):
            self.distance_incODO = 0
    
    def reset_speed(self):
        pass
    
    def stopwatch_start_stop(self):
        if(not self.locked):
            if(self.stopwatch_is_running):
                self.stopwatch_is_running = False
            else:
                self.stopwatch_is_running = True
                self.stopwatch_start = timer()   
    
    def stopwatch_reset(self):
        if(not self.locked):
            self.stopwatch_dt = 0
            self.stopwatch_start = self.stopwatch_stop
    
    def slow_update(self, dt):
        # Update the Clock
        self.clock_timeofday = time.strftime('%H : %M : %S')
        
        # Update the speeds (if connected)
        if(self.connection is not None and self.connection.is_connected()):
            speed_resp = self.connection.query(obd.commands.SPEED)
            
            if(not speed_resp.is_null()):
                speed = speed_resp.value.magnitude
                self.speed_time_new = speed_resp.time

            self.speed_Curr = str(speed)

            # Compute and update CAS
            CAS = (self.speed_Curr + self.speed_CAS)/2
            self.speed_CAS = CAS

            # Compute distance
            # distance (m) = speed (m/s) * time (s)
            if(not (self.speed_time_old is None)):
                dtime = self.speed_time_new - self.speed_time_old # in seconds
                
                dspeed = (speed*1000.0)/3600.0 # km/h to m/s

                #   km      1000 m      1 h       1 min       1000 m
                # ------ x -------- x -------- x -------- =  -------
                #   h        1 km      60 min     60 sec      3600 s
                
                # distance (m) = speed (m/s) * time (s)
                distance = dspeed * dtime

            # Add/Subtract to/from ODOs
            if(self.reverse_flag):
                self.distance_incODO -= distance
                self.distance_stageODO -= distance
            else:
                self.distance_incODO += distance
                self.distance_stageODO += distance

            

    def fast_update(self, dt):
        # Update the stopwatch, if it's running
        if(self.stopwatch_is_running):
            self.stopwatch_stop = timer()
            self.stopwatch_dt += self.stopwatch_stop - self.stopwatch_start
            self.stopwatch_start = self.stopwatch_stop
        
        # rounds to milliseconds for display
        self.stopwatch_disp = str(timedelta(seconds=round(self.stopwatch_dt,3)))[:-3] #chops empty microseconds
        
    def connect(self):
        if(self.connection is None):
            try:
                self.connection = obd.OBD(portstr='\\.\\COM5')
            except:
                print('OBD2 connection caused exception')
                e = sys.exc_info()[0]
                print('Error: ' + e)
            


class NavODOApp(App):
    def build(self):
        # return Label(text='Hello world')
        app = TestScreen()
        app.connect()
        Clock.schedule_interval(app.fast_update, 1.0/60.0)
        Clock.schedule_interval(app.slow_update, 1.0/3.0)
        return app

if __name__ == '__main__':
    NavODOApp().run()
