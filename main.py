import urllib.request
import matplotlib.pyplot as plt
import os

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Nie można znaleźć pliku:", file_path)
        return None

    return text


def generate_histogram_from_text(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            # char = char.lower()  #wyłączenie wielkich liter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


def save_histogram_to_file(letter_counts, output_file):
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


def read_text_from_url(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        return text
    except Exception as e:
        print("Błąd podczas pobierania tekstu", e)
        return ""


def generate_and_save(text, output_file):
    save_histogram_to_file(generate_histogram_from_text(text), output_file)


sciezka = os.getcwd()
file_path = sciezka + ('\\source_file.txt')
output_file = sciezka + ('\\histogram.png')
print("Wybierz skąd wprowadzić dane:")
print("1. Wprowadź z klawiatury.")
print("2. Podaj adres URL.")
print("3. Wczytaj z pliku source.txt")
option = input("Wybierz (1-2):")
text = ""
flag = True
while flag:
    if option == "1":
        flag = False
        text = input("Wprowadź tekst:")
        generate_and_save(text, output_file)

    elif option == "2":
        flag = False
        url = input("Wprowadź adres: ")
        text = read_text_from_url(url)
        generate_and_save(text, output_file)

    elif option == "3":
        flag = False
        text = read_text_from_file(file_path)
        generate_and_save(text,output_file)
    else:
        option = input("Błąd. Wybierz (1-2):")
