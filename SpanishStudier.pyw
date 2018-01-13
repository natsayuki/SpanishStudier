import tdl
import threading
import random
import json
import os
import sys
import numpy.core._methods
import numpy.lib.format
import tkinter as tk
from tdl import flush
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
conWidth = 80
conHeight = 50
con = tdl.init(conWidth, conHeight, title="Spanish Studier", fullscreen=False)
flush()
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vocab = {'el aire puro': 'clean air', 'el basurero': 'garbage container', 'la bioversidad': 'biodiversity', 'la capa de ozono': 'ozone layer', 'el clima': 'climate', 'la contaminacion': 'pollution'}
if getattr(sys, 'frozen', False):
    # frozen
    dir_ = os.path.dirname(sys.executable)
else:
    # unfrozen
    dir_ = os.path.dirname(os.path.realpath(__file__))

def center(row, text):
    con.draw_str(((conWidth/2)-(len(text)/2)), row, text)
def inCenter(row):
    var = ''
    while 1:
        k = tdl.event.key_wait()
        if k.key == 'ENTER':
            break
        elif k.key == 'BACKSPACE':
            var = var [:len(var)-1]
        elif k.shift and k.char:
            var += upper[lower.find(k.char)]
        else:
            var += k.char
        center(row, '                                                       ')
        center(row, var)
        flush()
    return var
def main():
    con.clear()
    correct = 0
    center(15, 'Set first terms to Spanish or English?')
    center(25, 'Spanish               English')
    con.draw_str(24, 25, '>')
    flush()
    answer = 1
    while 1:
        k = tdl.event.key_wait()
        if k.key == 'LEFT':
            answer -= 1
        elif k.key == 'RIGHT':
            answer += 1
        elif k.key == 'ENTER':
            if answer == 1:
                isSpanish = True
                questions = list(vocab)
            else:
                isSpanish = False
                questions = list(vocab.values())
            break
        answer %= 2
        if answer == 1:
            con.draw_str(46, 25, ' ')
            con.draw_str(24, 25, '>')
        else:
            con.draw_str(24, 25, ' ')
            con.draw_str(46, 25, '>')
        flush()
    con.clear()
    flush()
    center(15, 'Randomize vocab?')
    center(25, 'Yes         No')
    con.draw_str(32, 25, '>')
    flush()
    answer = 1
    while 1:
        k = tdl.event.key_wait()
        if k.key == 'LEFT':
            answer -= 1
        elif k.key == 'RIGHT':
            answer += 1
        elif k.key == 'ENTER':
            if answer == 1:
                mix = True
            else:
                mix = False
            break
        answer %= 2
        if answer == 1:
            con.draw_str(44, 25, ' ')
            con.draw_str(32, 25, '>')
        else:
            con.draw_str(32, 25, ' ')
            con.draw_str(44, 25, '>')
        flush()
    if mix:
        random.shuffle(questions)
    con.clear()
    flush()
    for i in questions:
        con.clear()
        center(15, i)
        flush()
        answer = inCenter(25)
        flush()
        if isSpanish:
            if answer == vocab[i]:
                center(30, 'correct')
                correct += 1
            else:
                center(30, 'the correct answer was "' + vocab[i] + '"')
        else:
            if answer == list(vocab.keys())[list(vocab.values()).index(i)]:
                center(30, 'correct')
                correct += 1
            else:
                center(30, 'the correct answer was "' + list(vocab.keys())[list(vocab.values()).index(i)] + '"')
        flush()
        while 1:
            k = tdl.event.key_wait()
            if k.key == "ENTER" or k.char == ' ':
                break
    center(30, 'you got ' + str(correct) + ' correct out of ' + str(len(vocab)))
    con.clear()
    center(15, 'practice again?')
    center(25, 'yes         no')
    con.draw_str(32, 25, '>')
    flush()
    answer = 1
    while 1:
        k = tdl.event.key_wait()
        if k.key == 'LEFT':
            answer -= 1
        elif k.key == 'RIGHT':
            answer += 1
        elif k.key == 'ENTER':
            if answer == 1:
                again = True
            else:
                again = False
            break
        answer %= 2
        if answer == 1:
            con.draw_str(44, 25, ' ')
            con.draw_str(32, 25, '>')
        else:
            con.draw_str(32, 25, ' ')
            con.draw_str(44, 25, '>')
        flush()
    if again:
        main()
    else:
        os._exit(1)
def start():
    center(25, "press ctrl+o to choose a voacb file")
    flush()
    while 1:
        k = tdl.event.key_wait()
        if k.keychar == 'o' and k.control:
            file = filedialog.askopenfilename(initialdir = os.path.realpath(dir_)+'/VocabLists', title = "Select vocab", filetypes = (("vocab files", '*.vocab'), ('json files', '*.json'), ('all files', '*.*')))

            if file == '':
                start()
            with open(file) as json_file:
                vocab = json.load(json_file)
            main()
def isDead():
    threading.Timer(.01, isDead).start()
    if tdl.event.is_window_closed():
        os._exit(1)
def isFull():
    threading.Timer(.01, isFull).start()
    k = tdl.event.key_wait()
    if k.key == "ESCAPE":
        tdl.set_fullscreen(not tdl.get_fullscreen())
isDead()
while not tdl.event.is_window_closed():
    start()
