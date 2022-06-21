#!/usr/bin/env python3
# coding=utf-8

from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
import sys

window = tk.Tk()
window.title("Welcome")
window.geometry("400x400")

def quit_window(icon, item):
    f = open("transfer.txt", "w")
    f.write("quit")
    f.close()
    window.destroy()
    icon.stop()

def show_window(icon, item):
    f = open("transfer.txt", "w")
    f.write("show_window")
    f.close()

def run():
  global window
  window.withdraw()
  image = Image.open("alarm4.ico")
  menu = (item('Quit', quit_window), item('Show', show_window))
  icon = pystray.Icon("name", image, "title", menu)
  icon.run()

if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])

