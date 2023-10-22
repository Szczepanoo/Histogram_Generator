import matplotlib
import matplotlib.pyplot as plt
import os
import tkinter as tk
matplotlib.use('TkAgg')
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


sciezka = os.getcwd()
output_file = sciezka + ('\\histogram.png')

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

def get_file_path():
    global file_path
    # Open and return file path
    file_path = fd.askopenfilename(title="Select A File",filetypes=(('text files', '*.txt'), ('All files', '*.*')))


# window
window = tk.Tk()
window.title('Histogram')
window.resizable(False, False)
window.geometry('300x150')
# widgets
b1 = tk.Button(window, text="Open File", command=get_file_path).pack(pady = 10)
b2 = Button(window, text = 'Zamknij okno i wyswietl histogram', command = window.destroy).pack(pady = 10)
# events
# run
window.mainloop()

letter_counts = generate_letter_histogram(file_path)
if letter_counts is not None:
    save_histogram_to_file(letter_counts, output_file)
