#!/usr/bin/env python3
# coding=utf-8

import tkinter as tk
from threading import *
import threading
import subprocess
import time
import os

window = tk.Tk()
window.title("Welcome")

proc = None

def withdraw_window():
  global proc
  proc = subprocess.Popen(["./tray.py run"], stdin=subprocess.PIPE,stdout=subprocess.PIPE, shell=True)
  stdout = proc.stdout
  x = threading.Thread(target=read_cmd, args=(stdout,))
  x.start()
  window.withdraw()

def read_cmd(stdout):
  while True:
    time.sleep(1)
    cmd = stdout.readline()
    print(cmd)
    if cmd == b'quit\n':
      os._exit(1)
    if cmd == b'show_window\n':
      window.deiconify()

def add():
  try:
    print('inicio')
    proc.communicate(timeout=1,input=b'abc')
  except subprocess.TimeoutExpired:
    print('ok')


button = tk.Button(window, text="Clean Alarms", command=lambda:add())
button.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

button = tk.Button(window, text="Close", command=lambda:withdraw_window())
button.place(relx=0.3, rely=0.9, anchor=tk.CENTER)

window.protocol('WM_DELETE_WINDOW', withdraw_window)
window.mainloop()