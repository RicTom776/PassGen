#!/usr/bin/python3

import os
import random



def all():
    allAlph = [
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","$","&","#","!","@","$","&","#"
    ]

    print("""
    Weak Password (1)
    Decent Password (2)
    Strong Password (3)
    -------------------
    EXIT (99)
    """)

    selectGen = input("Password Gen Type: ")



    def weakPass():
        global allRand1
        allRand1 = {allAlph[random.randint(0, 25)]+allAlph[random.randint(0, 25)]+allAlph[random.randint(0, 25)]+allAlph[random.randint(0, 25)]+allAlph[random.randint(26, 35)]+allAlph[random.randint(26, 35)]+allAlph[random.randint(26, 35)]+allAlph[random.randint(26, 35)]}

        print("Here is your weak password: "+''.join(allRand1))

    def decentPass():
        global allRand2
        allRand2 = {allAlph[random.randint(0, 25)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]+allAlph[random.randint(0, 47)]}

        print("Here is your decent password: "+''.join(allRand2))

    def strongPass():
        global allRand3
        allRand3 = {allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]+allAlph[random.randint(0, 71)]}

        print("Here is your strong password: "+''.join(allRand3))

    def savePass(filename, text):
        f = open(filename+".txt", "a")
        f.write(str(''.join(text)+"""
"""))

    if selectGen == "1":
        weakPass()
        savePass("weak-pass", allRand1)
        all()
    elif selectGen == "2":
        decentPass()
        savePass("decent-pass", allRand2)
        all()
    elif selectGen == "3":
        strongPass()
        savePass("strong-pass", allRand3)
        all()
    elif selectGen == "99":
        exit
    else:
        print("Kindly select the right gen type!")
        all()

all()
