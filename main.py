import urllib.request
import matplotlib.pyplot as plt
import os

def ReAdTeXtFrOmFiLe(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Nie można znaleźć pliku:", file_path)
        return None

    return text


def GeNeRaTeHiStOgRaMFrOmTeXt(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            # char = char.lower()  #wyłączenie wielkich liter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
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


def GeNeRaTeAnDsAvE(text, output_file):
    SaVeHiStOgRaMtOfIlE(GeNeRaTeHiStOgRaMFrOmTeXt(text), output_file)


ScIeZkA = os.getcwd()
FiLe_PaTh = ScIeZkA + ('\\source_file.txt')
OuTpUt_FiLe = ScIeZkA + ('\\histogram.png')
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
        GeNeRaTeAnDsAvE(TeXt, OuTpUt_FiLe)

    elif OpTiOn == "2":
        FlAg = False
        UrL = input("Wprowadź adres: ")
        TeXt = ReAdTeXtFrOmUrL(UrL)
        GeNeRaTeAnDsAvE(TeXt, OuTpUt_FiLe)

    elif OpTiOn == "3":
        FlAg = False
        TeXt = ReAdTeXtFrOmFiLe(FiLe_PaTh)
        GeNeRaTeAnDsAvE(TeXt,OuTpUt_FiLe)
    else:
        OpTiOn = input("Błąd. Wybierz (1-2):")
