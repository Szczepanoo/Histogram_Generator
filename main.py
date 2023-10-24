import matplotlib
import urllib.request
import matplotlib.pyplot as plt
import os
#from PIL import Image
import urllib.request
import tkinter as tk
matplotlib.use('TkAgg')
#from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
#from tkinter.messagebox import showinfo
#from PIL import Image,ImageTk
import urllib.request

def ReAdTeXtFrOmFiLe(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Nie można znaleźć pliku:", file_path)
        return None

    return text


def GeNeRaTeHiStOgRaMFrOmTeXt(text, chars):
    letter_counts = {}
    char_filter = set(chars)

    for char in text:
        if char.isalpha() and (not char_filter or char in char_filter):
            # char = char.lower()  # Opcjonalnie: zamiana na małe litery
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


def SaVeHiStOgRaMtOfIlE(letter_counts, output_file):
    if letter_counts is not None:
        letters = list(letter_counts.keys())
        counts = list(letter_counts.values())

        plt.bar(letters, counts)
        plt.xlabel('Litery')
        plt.ylabel('Liczba wystąpień')
        plt.title('Histogram częstotliwości liter')


        plt.xticks(letters)


        plt.savefig(output_file, format='png')
        plt.show()

        print("Zapisano histogram do pliku histogram.png")


def ReAdTeXtFrOmUrL(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        return text
    except Exception as e:
        print("Błąd podczas pobierania tekstu", e)
        return ""


# Funkcja generuje i zapisuje histogram
def GeNeRaTeAnDsAvE(text, chars, output_file):
    SaVeHiStOgRaMtOfIlE(GeNeRaTeHiStOgRaMFrOmTeXt(text, chars), output_file)


def ShOwHiStOgRaM(file_path):
    print("Czy chcesz usunąć plik histogram.png? (tak/nie)")
    OdP = input()
    if OdP.lower() == 'tak' or OdP.lower == 't':
        os.remove(OuTpUt_FiLe)
        print("Usunięto plik histogram.png")


ScIeZkA = os.getcwd()
FiLe_PaTh = ScIeZkA + ('\\source_file.txt')
OuTpUt_FiLe = ScIeZkA + ('\\histogram.png')
LiTeRy = ""
WyBoR = input("Czy chcesz korzystać z wersji konsolowej cz werjsi okienkowej? (konsola/okienko)")
FlAg = True
while FlAg:
    if WyBoR.lower() == "konsola" or WyBoR.lower() == "k":
        FlAg = False
        print("Domyślnie zliczane są wszystkie litery w tekście.")
        AnS = input("Czy chcesz podać listę liter do sprawdzenia? (tak/nie): ")
        LiTeRy = ""
        if AnS.lower() == "tak" or AnS.lower() == "t":
            LiTeRy = input("Podaj zestaw liter, oddziel poszczególne litery znakiem ','. Przykład: a,b,c : ")
            LiTeRy = LiTeRy.split(",")

        print("Wybierz skąd wprowadzić dane:")
        print("1. Wprowadź z klawiatury.")
        print("2. Podaj adres URL.")
        print("3. Wczytaj z pliku source.txt")
        OpTiOn = input("Wybierz (1-3):")
        TeXt = ""
        FlAg2 = True
        while FlAg2:
            if OpTiOn == "1":
                FlAg2 = False
                TeXt = input("Wprowadź tekst:")
                GeNeRaTeAnDsAvE(TeXt, LiTeRy, OuTpUt_FiLe)
                ShOwHiStOgRaM(OuTpUt_FiLe)

            elif OpTiOn == "2":
                FlAg2 = False
                UrL = input("Wprowadź adres: ")
                TeXt = ReAdTeXtFrOmUrL(UrL)
                GeNeRaTeAnDsAvE(TeXt, LiTeRy, OuTpUt_FiLe)
                ShOwHiStOgRaM(OuTpUt_FiLe)

            elif OpTiOn == "3":
                FlAg2 = False
                TeXt = ReAdTeXtFrOmFiLe(FiLe_PaTh)
                GeNeRaTeAnDsAvE(TeXt, LiTeRy, OuTpUt_FiLe)
                ShOwHiStOgRaM(OuTpUt_FiLe)

            else:
                OpTiOn = input("Błąd. Wybierz (1-3):")
    elif WyBoR == "okienko" or WyBoR == "o":
        FlAg = False
        # window
        window = tk.Tk()
        window.title('Histogram')
        window.resizable(False, False)
        window.geometry('600x150')
        # widgets
        mystring = tk.StringVar(window)
        mystring2 = tk.StringVar(window)


        def GeTfIlEpAtH():
            global file_path
            # Open and return file path
            file_path = fd.askopenfilename(title="Select A File", filetypes=(('text files', '*.txt'), ('All files', '*.*')))
            TeXt = ReAdTeXtFrOmFiLe(FiLe_PaTh)
            GeNeRaTeAnDsAvE(TeXt, LiTeRy, OuTpUt_FiLe)


        def getvalueURL():
            val = mystring.get()
            text = ReAdTeXtFrOmUrL(val)
            GeNeRaTeAnDsAvE(text, LiTeRy, OuTpUt_FiLe)

        def getvalueTXT():
            val = mystring2.get()
            GeNeRaTeAnDsAvE(val, LiTeRy, OuTpUt_FiLe)


        label = Label(window, text="Wybierz plik:")
        label.place(x=40, y=20)
        b1 = tk.Button(window, text="Wyświetl histogram z pliku", command=GeTfIlEpAtH)
        b1.place(x=160, y=20)
        label2 = Label(window, text="Wprowadź url:")
        label2.place(x=40, y=60)
        inp = Entry(window, width=20, textvariable=mystring)
        inp.place(x=160, y=60)
        b2 = Button(window, text="Wyświetl histogram z url" , command=getvalueURL)
        b2.place(x=320, y=55)
        label3 = Label(window, text="Wprowadź url:")
        label3.place(x=40, y=100)
        inp = Entry(window, width=20, textvariable=mystring2)
        inp.place(x=160, y=100)
        b3 = Button(window, text="Wyświetl histogram z wprowadzonego textu", command=getvalueTXT)
        b3.place(x=320, y=95)



        # events
        # run
        window.mainloop()
    else:
        WyBoR = input("Wpisz 'konsola' lub 'okienko' dla odpowiedniego trybu wyświetlania: ")
