import pyautogui as pyag
import keyboard as kb
from wonderwords import RandomWord
import time

# url x = 751, y = 53
# remove 702, 17
# add 491, 20

urlx = 751
urly = 53

remx = 702
remy = 17

addx = 491
addy = 20

while True:
    time.sleep(5)
    rwg = RandomWord()

    pyag.click(urlx, urly)

    kb.write(rwg.random_words())
    kb.write(" ")
    kb.press_and_release('Backspace')
    kb.press_and_release('Enter')

    time.sleep(5)
    pyag.click(remx, remy)
    
    time.sleep(1)
    pyag.click(addx, addy)