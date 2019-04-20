STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

#FOREGROUND_BLACK = 0x00
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN = 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN = 0x20 # background color contains green.
BACKGROUND_RED = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
  bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
  return bool

import time
import os
import random

def tprint(string='', t = 0.045, newLine = 0.4, ends='\n'):
  for i in str(string).split(sep="\n"):
    for j in i:
      print(end = j)
      time.sleep(t)
    time.sleep(newLine)
    print()
  print(end=ends)

def curtainClose(string, shell='on'):
  if shell == 'on':
    os.system("cls")
  print()
  front = ""
  back = ""
  space = 0
  for i in range(len(string)):
    print(end = '\n\n\n')
    print(end = '                   ')
    front += string[i]
    back = string[-1-i] + back
    nospace = len(string)*2
    space = nospace - len(front+back)*2
    set_color(random.randint(0, 15))
    if len(string) % 2 != 0 and space < 0:
      print(front+" "*space+back[1:])
      #curtainClose(string, shell)
      break
    else:
      print(front+" "*space+back)
    if space == 0:
      #curtainClose(string, shell)
      break
    time.sleep(0.1)
    if shell == 'on':
      os.system("cls")
    print()

def curtainOpen(string, shell='on'):
  if shell == 'on':
    os.system("cls")
  print()
  if len(string) % 2 != 0:
    front = len(string)-1
    middle = len(string) // 2
    midplus = middle + 1
  else:
    front = len(string)-2
    middle = len(string) // 2 - 1
    midplus = middle + 2
  for i in range(len(string)):
    print(end = '\n\n\n')
    print(end = '                   ')
    set_color(random.randint(0, 15))
    print(" "*front + string[middle:midplus])
    front -= 2
    middle -= 1
    midplus += 1
    if middle == 0:
      #print(string)
      break
    time.sleep(0.1)
    if shell == 'on':
      os.system("cls")
    print()

def OAC(string, shell='on'):
  curtainOpen(string, shell)
  curtainClose(string, shell)
  set_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
  OAC(string, shell)

while True:
  ask = input("띄어쓰기 없이 한글 문자열을 하나 입력하세요.")
  OAC(ask)
