import os
import string
import matplotlib.pyplot as plt

def generate_histogram(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def plot_histogram(letter_count, output_file):
    letters = list(letter_count.keys())
    counts = list(letter_count.values())

    plt.figure(figsize=(12, 6))
    plt.bar(letters, counts)
    plt.xlabel('Litera')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram częstości występowania liter')
    plt.savefig(output_file)
    plt.show()

def main(input_dir, output_file):
    letter_count = {}
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    text = f.read()
                    letter_count.update(generate_histogram(text))

    if output_file.endswith(".txt"):
        with open(output_file, "w", encoding="utf-8") as f:
            for letter, count in sorted(letter_count.items()):
                f.write(f"{letter}: {count}\n")
    elif output_file.endswith(".jpg") or output_file.endswith(".png"):
        plot_histogram(letter_count, output_file)
    else:
        print("Nieobsługiwany format wyjściowy. Wspierane formaty to .txt, .jpg i .png.")

if __name__ == "__main__":
    input_directory = "C:\jakub.szczepanski\żżż_inne\DUPADUPA\dupa1"
    output_file = "C:\jakub.szczepanski\żżż_inne\DUPADUPA\histogram.jpg"
    main(input_directory, output_file)
