STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLACK = 0x00
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN = 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
#BACKGROUND_BLUE = 0x10 # background color contains blue.
#BACKGROUND_GREEN = 0x20 # background color contains green.
#BACKGROUND_RED = 0x40 # background color contains red.
#BACKGROUND_INTENSITY = 0x80 # background color is intensified.

import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
  bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
  return bool

import random
import os
import time

bar = ["██", "  "]


def Music(row=6, column=6):
  lineMaker = [[]]*row
  lines = []
  checkStart = 0
  music = []
  while True:
    for i in lineMaker:
      if checkStart == 0:
        checker = []
      else:
        pass
      i = [bar[random.randint(0, 1)] for _ in range(0, column)]
      for k in checker:
        i[k] = "██"
      for j in range(len(i)):
        try:
          checker.append(i.index("██", j))
        except ValueError:
          pass
      checker = list(set(checker))
      checkStart = 1
      lines.append(i)
    break
  for i in lines:
    text = ""
    for j in i:
      text = text + ' ' + j
    music.append(text[1:])
  return music

def MusicStart(row=6, column=6, shell='on', color='on'):
  while True:
    if shell == 'on':
      os.system("cls")
    print("\n\n\n\n\n")
    for i in Music(row, column):
      if color == 'on':
        set_color(random.randint(1, 15))
        print("                    "+i)
        set_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
      else:
        print("                    "+i)        
    time.sleep(0.08)

ask = input("Option : ")
MusicStart(color=ask)
