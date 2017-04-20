from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from time import strftime
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class ClockApp(App):

    sw_seconds = 0
    minutes = 0
    seconds = 0
    def update_time(self, nap):
        self.root.time_prop.text = strftime('[b]%H[/b]:%M:%S')
        if self.root.button_start.text == 'Stop':
            self.sw_seconds += nap
        self.minutes, self.seconds = divmod(self.sw_seconds,60)
        self.root.sw_display_seconds.text = '%02d:%02d.[size=40]%02d[/size]' % (int(self.minutes), int(self.seconds), int(self.seconds* 100 % 100))
    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
    def start_stop(self):
        print self.root.button_start.text
        if self.root.button_start.text == 'Stop':
            self.root.button_start.text = 'Start'
        else:
            self.root.button_start.text = 'Stop'
    def reset(self):
        if self.root.button_start.text == 'Stop':
            self.root.button_start.text = 'Start'
        self.sw_seconds = 0

    




class ClockRoot(BoxLayout):
    time_prop = ObjectProperty()
    sw_display_seconds = ObjectProperty()

    pass

if __name__ == '__main__':
    ClockApp().run()
