import time
import pyautogui as pauto
import keyboard
msw_text_full = """
TO rect :b :h
  pd
  repeat 2 [fd :h rt 90 fd :b rt 90]
  pu
END

TO tri :l
  pd
  lt 90
  fd :l * 0.5
  rt 180 - 63
  fd :l * 1.11803398875
  rt 180 - 54
  fd :l * 1.11803398875
  rt 180 - 63
  fd :l * 1
  bk :l * 0.5
  rt 90
  pu
END

TO fillFR :color
  setfloodcolor :color
  rt 45
  fd 3
  fill
  bk 3
  lt 45
  setfloodcolor 0
END
"""
msw_text_full = """
setpencolor 0
showturtle
pd
ellipse 100 50
pu

fd 50
lt 90
fd 10
rt 90
rect 20 20
fillFR 15

fd 20
lt 90
fd 190
rt 90
rect 400 10
fillFR 15
bk 130
rt 90
fd 100
lt 90

rect 200 10
fillFR 15

rt 90
fd 100
lt 90
fd 55
rect 200 10

bk 10
rt 90
fd 200
lt 90

setpencolor 1


tri 40

setpencolor 0
pu
lt 15
fd 7
setfloodcolor 0
fill 
fd 5 
fill
setfloodcolor 15
fill
bk 12
rt 15
setpencolor 0
setfloodcolor 0

tri 40

lt 90
fd 250
rt 90
fd 38
pd
ellipse 20 20
pu
setfloodcolor 3
fill
setfloodcolor 0


pu
setfloodcolor 0
bk 25
fill
rt 90
fd 80
fill
fd 100
fillFR 15
"""

pauto.PAUSE = 0.01
msw_list = msw_text_full.split("\n")


stopprog = False
keyboard.add_hotkey('p', lambda: writeProg())
keyboard.add_hotkey('m', lambda: doexit())


def writeProg():
    pauto.write('u')
    pauto.press("enter")
    for line in msw_list:
        pauto.write(line)
        pauto.press("enter")


def doexit():
    global stopprog
    stopprog = True


print("started")
while not stopprog:
    time.sleep(0.1)
print("ended")
