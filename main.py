from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,StringProperty, \
    BooleanProperty
from kivy.clock import Clock
import time
from time import monotonic as timer
from datetime import timedelta 


class TestScreen(Widget):
    # Timing and Clock
    clock_timeofday = StringProperty()
    stopwatch_dt = StringProperty('')
    stopwatch_start = timer()
    stopwatch_stop = stopwatch_start
    stopwatch_is_running = BooleanProperty(False)


    # Speeds
    speed_CAS = NumericProperty(0)
    speed_Curr = NumericProperty(0)

    # Distances
    distance_incODO = NumericProperty(0)
    distance_stageODO = NumericProperty(0)

    def test_callback(self):
        print('button push')

    def zero_CAS(self):
        pass
    
    def zero_stageODO(self):
        pass
    
    def zero_incODO(self):
        pass
    
    def reset_speed(self):
        pass
    
    def stopwatch_start_stop(self):
       
        if(self.stopwatch_is_running):
            self.stopwatch_stop = timer()
            self.stopwatch_is_running = False
        else:
            self.stopwatch_is_running = True
            if(self.stopwatch_start ==  self.stopwatch_stop):
                self.stopwatch_start = timer()
                self.stopwatch_stop = self.stopwatch_start
    
    def stopwatch_reset(self):
        self.stopwatch_start = timer()
        self.stopwatch_start = self.stopwatch_stop
    

    def update(self, dt):
        # Update the Clock
        self.clock_timeofday = time.strftime('%H : %M : %S')
        
        # Update the stopwatch, if it's running
        if(self.stopwatch_is_running):
            self.stopwatch_stop = timer()
        
        self.stopwatch_dt = str(timedelta(seconds=self.stopwatch_stop-self.stopwatch_start))
        


class NavODOApp(App):
    def build(self):
        # return Label(text='Hello world')
        app = TestScreen()
        
        Clock.schedule_interval(app.update, 1.0/3.0)
        return app


if __name__ == '__main__':
    NavODOApp().run()
