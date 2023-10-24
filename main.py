import urllib.request
import matplotlib.pyplot as plt
import os
from PIL import Image

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
            #char = char.lower()  # Opcjonalnie: zamiana na małe litery
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

#Funkcja generuje i zapisuje histogram
def GeNeRaTeAnDsAvE(text, chars, output_file):
    SaVeHiStOgRaMtOfIlE(GeNeRaTeHiStOgRaMFrOmTeXt(text, chars), output_file)


def ShOwHiStOgRaM(file_path):
    FoTo = Image.open(file_path)
    FoTo.show()


ScIeZkA = os.getcwd()
FiLe_PaTh = ScIeZkA + ('\\source_file.txt')
OuTpUt_FiLe = ScIeZkA + ('\\histogram.png')
print("Domyślnie liczane są wszystkie litery w tekście.")
AnS = input("Czy chcesz podać listę liter do sprawdzenia? (tak/nie): ")
LiTeRy = ""
if AnS.lower() == "tak" or AnS.lower() == "t":
    LiTeRy = input("Podaj zestaw liter, oddziel poszczególne litery znakiem ','. Przykład: a,b,c : ")
    LiTeRy = LiTeRy.split(",")


print("Wybierz skąd wprowadzić dane:")
print("1. Wprowadź z klawiatury.")
print("2. Podaj adres URL.")
print("3. Wczytaj z pliku source.txt")
OpTiOn = input("Wybierz (1-2):")
TeXt = ""
FlAg = True
while FlAg:
    if OpTiOn == "1":
        FlAg = False
        TeXt = input("Wprowadź tekst:")
        GeNeRaTeAnDsAvE(TeXt, LiTeRy, OuTpUt_FiLe)
        ShOwHiStOgRaM(OuTpUt_FiLe)
        print("Czy chcesz usunąć plik histogram.png? (t/n)")
        OdP = input()
        if OdP == 't':
            os.remove(OuTpUt_FiLe)
            print("Usunięto plik histogram.png")

    elif OpTiOn == "2":
        FlAg = False
        UrL = input("Wprowadź adres: ")
        TeXt = ReAdTeXtFrOmUrL(UrL)
        GeNeRaTeAnDsAvE(TeXt, LiTeRy, OuTpUt_FiLe)
        ShOwHiStOgRaM(OuTpUt_FiLe)
        print("Czy chcesz usunąć plik histogram.png? (t/n)")
        OdP = input()
        if OdP == 't':
            os.remove(OuTpUt_FiLe)
            print("Usunięto plik histogram.png")

    elif OpTiOn == "3":
        FlAg = False
        TeXt = ReAdTeXtFrOmFiLe(FiLe_PaTh)
        GeNeRaTeAnDsAvE(TeXt, LiTeRy, OuTpUt_FiLe)
        ShOwHiStOgRaM(OuTpUt_FiLe)
        print("Czy chcesz usunąć plik histogram.png? (t/n)")
        OdP = input()
        if OdP == 't':
            os.remove(OuTpUt_FiLe)
            print("Usunięto plik histogram.png")
    else:
        OpTiOn = input("Błąd. Wybierz (1-2):")