import urllib.request
import matplotlib.pyplot as plt
def generate_letter_histogram(file_path):
    letter_counts = {}
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            for char in text:
                if char.isalpha():
                    char = char.lower()
                    if char in letter_counts:
                        letter_counts[char] += 1
                    else:
                        letter_counts[char] = 1
    except FileNotFoundError:
        print("Nie można znaleźć pliku:", file_path)
        return None

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

def read_text_from_url(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        return text
    except Exception as e:
        print("Błąd podczas pobierania tekstu", e)
        return ""


file_path = 'C:\\jakub.szczepanski\\Semestr III\\Specjalistyczne Oprogramowanie Narzędziowe\\Ćwiczenia\\SON_Projekt1\\source_file.txt'
output_file = 'C:\\jakub.szczepanski\\Semestr III\\Specjalistyczne Oprogramowanie Narzędziowe\\Ćwiczenia\\SON_Projekt1\\histogram.png'

print("Wybierz skąd wprowadzić dane:")
print("1. Wprowadź z klawiatury.")
print("2. Podaj adres URL.")
option = input("Wybierz (1-2):")
text = ""
flag = True
while flag:
    if option == "1":
        flag = False
        text = input("Wprowadź tekst:")
        letter_counts = {}

        for char in text:
            if char.isalpha():
                #char = char.lower()  #wyłączenie wielkich liter
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1

        save_histogram_to_file(letter_counts,output_file)
        print("Zapisano histogram do pliku histogram.png")

    elif option == "2":
        flag = False
        url = input("Wprowadź adres: ")
        text = read_text_from_url(url)
        ge

    else:
        option = input("Błąd. Wybierz (1-2):")



'''
letter_counts = generate_letter_histogram(file_path)
if letter_counts is not None:
    save_histogram_to_file(letter_counts, output_file)
    print("Zapisano histogram do pliku histogram.png")
    '''