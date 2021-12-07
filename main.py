from math import *
import tkinter as tk
from threading import Thread
# my programing launguage

print("Welcome to v programing language (vpl)\n ©️all rights reserved")

def pl():
    com = input("➡️-  ")

#print
    if com == "printv":
        printv = input("printv:-")
        print(printv)
#calulatio prosses(code start)
    elif com == "+":
        st = input("1st:-")
        nd = input("2nd:-")
        answer = float(st) + float(nd)
        print(answer)
    elif com == "-":
        st = input("1st:-")
        nd = input("2nd:-")
        answer = float(st) - float(nd)
        print(answer)
    elif com == "/":
        st = input("1st:-")
        nd = input("2nd:-")
        answer = float(st) / float(nd)
        print(answer)
    elif com == "*":
        st = input("1st:-")
        nd = input("2nd:-")
        answer = float(st) * float(nd)
        print(answer)
    elif com == "**":
        st = input("1st:-")
        nd = input("2nd:-")
        answer = float(st) ** float(nd)
        print(answer)
    elif com == "//":
        st = input("1st:-")
        nd = input("2nd:-")
        answer = float(st) // float(nd)
        print(answer)
    # calulatio prosses(code end)
    elif com == "lenv":
        lenv = input("word:-")
        print(len(lenv))
    elif com == "vpl --dev":
        print("⚫ Vishwa Poornaka Amarasinghe \n⚫ Jaysanka Weerasinghe")
    elif com == "vpl --version":
        version = "1.0.0"
        print(version)
    elif com == "lowerv":
        lowerv = input("lowerv:-")
        print(lowerv.lower())
    elif com == "upperv":
        upperv = input("upperv:-")
        print(upperv.upper())
    elif com == "islowerv":
        islowerv = input("islowerv:-")
        print(islowerv.islower())
    elif com == "isupperv":
        isupperv = input("isupperv:-")
        print(isupperv.isupper())
    elif com == "replacev":
        replacev = input("replacev:-")
        re = input("what do yo want to replace:-")
        ren = input("enter the word/sentencs:-")
        print(replacev.replace(re, ren))
    elif com == "indexv":
        indexv = input("indexv:-")
        indexn = input("the word/sentence that you want to index:-")
        print(indexv.index(indexn))
    elif com == "powv":
        print(pow(int(input("powv 1st number-")), int(input("powv 2nd number-"))))
    elif com == "roundv":
        roundv = float(input("roundv:-"))
        print(round(roundv))
    elif com == "-roundv":
        roundvm = float(input("-roundv:-"))
        print(-round(roundvm))
    elif com == "absv":
        absv = float(input("absv:-"))
        print(abs(absv))
        #jaye aiyya meka thama palleha thiyenne code eka
    elif com == "maxv":
        maxv = input("maxv:-")
        print(max(maxv))
    elif com == "sqrtv":
        sqrtv = float(input("sqrtv:-"))
        print(sqrt(sqrtv))
    elif com == "ceilv":
        ceilv = float(input("ceilv:-"))
        print(ceil(ceilv))
    elif com == "floorv":
        floorv = float(input("floorv:-"))
        print(floor(floorv))
    elif com == "facv":
        facv = int(input("facv:-"))
        print(factorial(facv))
    elif com == "floatv":
        floatv = input("floatv:-")
        print(float(floatv))
    elif com == "comv":
        comv = input("#")
        print("comment added")
    elif com == "inv":
        text = input("text:-")
        word = input("word that you find:-")
        print(word in text)
    elif com == "notinv":
        text = input("text:-")
        word = input("word that you find:-")
        print(word not in text)
    elif com == "listv":
        listv = [input("enter the list:-")]
        print(listv)
    elif com =="clearv":
        listv = [input("listv:-")]
        listv.clear()
        print(listv)
        print("list cleared")
    elif com == "for in v":
        forv = input("words-")
        for word in forv:
            print(word)
    elif com == "rangev":
        num = int(input("1st number:-"))
        num2 = int(input("2nd number:-"))
        for number in range(num, num2):
            print(number)
    elif com == "windowv":
        print("when you create this window you are unable to use vpl until you close this window")
        canvas = tk.Tk()
        size = input("size of window:-")
        title = input("title of the window:-")
        color = input("color of window:-")
        txt = input("text:-")
        t = ("poppins", 35, "bold")
        label1 = tk.Label(canvas, font=t)
        label1.pack()
        label1.config(bg=color)
        label1.config(text=txt)
        canvas.title(title)
        canvas.geometry(size)
        canvas.config(bg=color)
        Thread(target=canvas.mainloop()).start()
        Thread(target=pl()).start()






    else:
        print("wrong code please try again")
        pl()



try:
    pl()
except:
    print("write a correct command this not valid")
try:
    pl()
except ValueError:
    print("write a correct command this not valid")
try:
    pl()
except TypeError:
    print("write a correct command this not valid")
try:
    pl()
except SyntaxError:
    print("write a correct command this not valid")
try:
    pl()
except FloatingPointError:
    print("write a correct command this not valid")
pl()


