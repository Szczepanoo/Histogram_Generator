import matplotlib.pyplot as plt
import os
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

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

def ShowHistogram(file_path):
    foto = Image.open(file_path)
    foto.show()

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

#window
window = tk.Tk()
window.title('Tkinter Open File Dialog')
window.resizable(False, False)
window.geometry('600x600')

#widgets
open_button = ttk.Button(
    window,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)
#events
#run
window.mainloop()

sciezka = os.getcwd()
file_path = sciezka+('\\source_file.txt')
output_file = sciezka+('\\histogram.png')
letter_counts = generate_letter_histogram(file_path)
if letter_counts is not None:
    save_histogram_to_file(letter_counts, output_file)
    print("Zapisano histogram do pliku histogram.png")
    ShowHistogram(output_file)
    print("Czy chcesz usunąć plik histogram.png? (t/n)")
    odp = input()
    if odp == 't':
        os.remove(output_file)
        print("Usunięto plik histogram.png")