#!/usr/bin/env python3
# coding=utf-8

import sys
import time
import fileinput

def run():
  i = 1
  while i < 3:
    time.sleep(1)
    print(f'ok {i}', flush=True)
    i+=1
  time.sleep(1)
  print(f'end', flush=True)
  time.sleep(1)
  data = sys.stdin.readline()
  #line = fileinput.readline()
  print(data, flush=True)
  print('full', flush=True)

if __name__ == "__main__":
    run()
