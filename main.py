import matplotlib as plt
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

        # Ustaw etykiety na osi X
        plt.xticks(letters)

        # Zapisz histogram do pliku PNG lub JPG
        plt.savefig(output_file, format='png')  # Zmień 'png' na 'jpg' jeśli chcesz format JPG
        plt.show()