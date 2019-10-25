#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import tkinter
import datetime
import os
import sys

class ClockGUI:
    def __init__(self):
        '''Constructor for GUI'''
        self.root_window = tkinter.Tk()
        self.root_window.geometry("350x200")
        self.root_window.title("Digital Clock")
        self.root_window.resizable(0, 0)
        #self.root_window.iconbitmap(self.resource_path(""))
        self.show_time = tkinter.StringVar()

    def get_time(self) -> str:
        '''Gets the current time'''
        time = datetime.datetime.now()
        pm = False
        if time.hour > 12:
            pm = True
        if pm:
            self.show_time.set("{}:{}:{} P.M.".format(time.hour-12, time.minute, time.second))
            return "{}:{}:{}".format(time.hour-12, time.minute, time.second)
        else:
            self.show_time.set("{}:{}:{} A.M.".format(time.hour, time.minute, time.second))
            return "{}:{}:{}".format(time.hour, time.minute, time.second)

    def run(self) -> None:
        '''Runs the GUI'''
        self.display_time = tkinter.Label(self.root_window, textvariable = self.show_time)
        self.show_time.set(self.get_time())
        self.display_time.pack(side = tkinter.TOP)
        self.root_window.mainloop()


if __name__ == "__main__":
    ClockGUI().run()