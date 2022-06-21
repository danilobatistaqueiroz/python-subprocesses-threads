#!/usr/bin/env python3
# coding=utf-8

from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
from threading import *
import threading
import subprocess
import pickle
import multiprocessing
import time
from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager
import sys, os

window = tk.Tk()
window.title("Welcome")

f = open("transfer.txt", "w")
f.write("")
f.close()

proc = None

def withdraw_window():
  global proc
  if proc == None:
    proc = subprocess.Popen(["./icone.py","run",], stdout=subprocess.PIPE)
    x = threading.Thread(target=read_transfer, args=())
    x.start()
  window.withdraw()

def read_transfer():
  while True:
    time.sleep(1)
    f = open("transfer.txt", "r")
    text = f.read()
    f.close()
    print(f'reading {text}')
    if text == 'quit':
      os._exit(1)
    if text == 'show_window':
      f = open("transfer.txt", "w")
      f.write("")
      f.close()
      window.deiconify()

window.protocol('WM_DELETE_WINDOW', withdraw_window)
window.mainloop()