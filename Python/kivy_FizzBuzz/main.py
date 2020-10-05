# FizzBuzz with Kivy GUI
# Author: Franklin Ikeh
import time
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex as hexColor

Window.clearcolor = hexColor("#DDDDFF") # change window color


class FizzBuzzApp(App):
    # some useful variables
    started = False
    finished = False
    number = 1

    def update_fb(self, nap):
        """
        This method updates the numbers,
         shown on the screen each time it is called
        """
            
        if self.started:

            def current_num(number, show_num=False):
                """
                This function determines whether the current number is
                fizz, buzz or fizzbuzz
                """
                
                if number % 3 == 0 and number % 5 == 0:
                    return f"[color=#FF00AA]Fizz[/color][color=#DD00DD]Buzz[/color]"

                elif number % 3 == 0:
                    return f"[color=#00BB00]Fizz[/color]"
                    
                elif number % 5 == 0:
                    return f"[color=#EE0000]Buzz[/color]"

                else:
                    # whether to show the current number or not
                    if show_num:
                        return number
                    else:
                        return ""

            self.root.ids.fb_scr.text = str(current_num(self.number))
            self.root.ids.num_scr.text = str(self.number)
            self.root.ids.fb_num_scr.text = (
                self.root.ids.fb_num_scr.text + "    " + str(current_num(self.number, True))
            )

            if self.number < 100:
                # increment the number after each function call
                self.number += 1

            elif self.number == 100:
                self.started = not self.started # stop the loop
                self.root.ids.start_btn.text = "Start"
                self.number = 1 # reset the number
                self.finished = True

    def start_stop(self):
        """ This method starts, stop, pause or continues the program"""
        
        if self.finished:
            self.root.ids.fb_num_scr.text = "" # clear the label
            self.started, self.finished = True, False

        else:
            self.started = not self.started

        if self.started == False and self.number < 100:
            self.root.ids.start_btn.text = "Continue"
            
        elif self.started == True:
            self.root.ids.start_btn.text = "Pause"

    def on_start(self):
        Clock.schedule_interval(self.update_fb, .35)


if __name__ == "__main__":
    FizzBuzzApp().run()
