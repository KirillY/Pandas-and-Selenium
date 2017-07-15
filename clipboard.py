from tkinter import Tk
# from msvcrt import getch
import win32con
import win32api
import time

while True:
    # key = ord(getch())
    # if key == 27: #ESC
    if win32api.GetAsyncKeyState(ord('Q')):
        break
   
    elif win32api.GetAsyncKeyState(ord('C')) and win32api.GetAsyncKeyState(win32con.VK_LCONTROL):
        # print(type(win32api.GetAsyncKeyState(win32con.VK_LCONTROL)), win32api.GetAsyncKeyState(ord('C')))
        print(Tk().clipboard_get())
        time.sleep(1)
        # Tk().clipboard_clear()


     

