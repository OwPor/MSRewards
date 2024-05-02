# python -m PyInstaller main.py --windowed --onefile --icon="icon.ico"
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.font import Font
import pyautogui as pyag
import keyboard as kb
from pynput import keyboard, mouse
import random

urlx = 0
urly = 0
total = 0
scheduled_event = None

def urlPos(key):
    global urlx, urly

    try:
        if key.char == 'k':
            urlx, urly = mouse.Controller().position
            return False
    except AttributeError:
        pass

def getUrlPos():
    listener = keyboard.Listener(on_press=urlPos)
    listener.start()
    listener.join()
    mb.showinfo('URL Position', 'X: ' + str(urlx) + ', Y: ' + str(urly))

def search(times):
    
    def perform_action():
        with open('words.txt', 'r') as f:
            l = next(f)
            for num, line in enumerate(f, 2):
                if random.randrange(num):
                    continue
                l = line
        global running, scheduled_event
        nonlocal i
        
        rwg = l
        pyag.click(urlx, urly)
        kb.write(rwg)
        kb.write(' ')
        kb.press_and_release('Backspace')
        kb.press_and_release('Enter')
        i += 1
        global total
        total = i
        if not running or i >= times:
            if i >= times:
                root.after(1000)
                mb.showinfo('Done!', 'Times: ' + str(times))
            return
        scheduled_event = root.after(delay, perform_action)
    i = 0
    perform_action()

def start():
    global running, counts, delay
    running = True
    counts = sp.get()
    delay = de.get()

    if int(counts) == 0:
        mb.showinfo('Times', 'Enter how many times first')
        return
    
    if int(delay) == 0:
        mb.showinfo('Delay', 'Enter delay time first')
        return

    delay = int(delay) * 1000  
    
    if urlx == 0 and urly == 0:
        mb.showinfo('Set Position', 'Set positions first')
        return
    
    bool(search(int(counts)))

def cancel():
    global running, scheduled_event
    running = False
    if scheduled_event is not None:
        root.after_cancel(scheduled_event)
    mb.showinfo('Done!', 'Times: ' + str(total))

root = tk.Tk()
root.resizable(False, False)
root.geometry('300x350')
root.iconbitmap('icon.ico')
root.title('Auto Search by OwPor')

label = tk.Label(root, text='How many times?:', font=('Times New Roman', 12))
label.pack(padx=10, pady=8)
sp = tk.Spinbox(root, width=5, from_=0, to=100, wrap=True, font=Font(family='Helvetica', size=14))
sp.pack()

label = tk.Label(root, text='Delay:', font=('Times New Roman', 12))
label.pack(padx=10, pady=8)
de = tk.Spinbox(root, width=5, from_=0, to=100, wrap=True, font=Font(family='Helvetica', size=14))
de.pack()

label = tk.Label(root, text='Press K when button is clicked to set position', font=('Times New Roman', 12))
label.pack(padx=10, pady=8)

url_btn = tk.Button(root, text='Set URL Pos', command=getUrlPos, font=('Times New Roman', 12))
url_btn.pack(padx=10, pady=8)

start_btn = tk.Button(root, text='Start', command=start, font=('Times New Roman', 12))
start_btn.pack(padx=10, pady=8)

cancel_btn = tk.Button(root, text='Cancel', command=cancel, font=('Times New Roman', 12))
cancel_btn.pack(padx=10, pady=8)

root.mainloop()
