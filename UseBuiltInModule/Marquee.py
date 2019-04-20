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

import os
import time

def Marquee(string):
  space = " "*50
  for i in range(len(string)):
    os.system("cls")
    print("\n\n\n\n")
    print(space + string[:1+i])
    time.sleep(0.05)
    space = space[:-1-i]
  j = i
  while True:
    os.system("cls")
    print("\n\n\n\n")
    print(space + string)
    time.sleep(0.05)
    space = space[:-1-j]
    j += 1
    if len(space) == 0:
      for i in range(len(string)):
        os.system("cls")
        print("\n\n\n\n")
        print(string[i:])
        time.sleep(0.05)
      Marquee(string)

Marquee(input("아무 단어나 문장을 입력하세요."))
