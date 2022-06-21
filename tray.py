#!/usr/bin/env python3
# coding=utf-8

import os
import threading
from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
import sys
import time
from notifypy import Notify

window = tk.Tk()
window.title("Welcome")
window.geometry("400x400")

proc = None
icon = None

def quit_window(icon, item):
    print('quit', flush=True)
    window.destroy()
    icon.stop()

def show_window(icon, item):
    print('show_window', flush=True)
    #icon.stop()
    #window.deiconify()
    #os._exit(1)

def run():
  #global window
  #window.withdraw()
  image = Image.open("alarm4.ico")
  menu = (item('Quit', quit_window), item('Show', show_window))
  x = threading.Thread(target=read_cmd, args=())
  x.start()
  #read_cmd()
  global icon
  icon = pystray.Icon("name", image, "title", menu)
  icon.run()

def read_cmd():
    for line in sys.stdin:
      if line.find('abc')>-1:
        show_notify('stop')
        global icon
        icon.stop()
        # print(line, flush=True)
        image = Image.open("alarm4.ico")
        menu = (item('Quit', quit_window), item('Show', show_window), item('Ok', show_window))
        icon = pystray.Icon("name", image, "title", menu)
        icon.run()
    print('fim',flush=True)


def show_notify(description):
    notification = Notify()
    notification.title = "Alarm"
    notification.message = description
    notification.icon = "alarm4.png"
    notification.audio = "mixkit-gaming-lock-2848.wav"
    notification.send()


if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])

def withdraw_window():
  pass

window.protocol('WM_DELETE_WINDOW', withdraw_window)
window.mainloop()