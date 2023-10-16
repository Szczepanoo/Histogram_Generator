def generate_letter_histogram(file_path):
    letter_counts = {}

    try:
        with open(file_path, 'r') as file:
            text = file.read()
            for char in text:
                if char.isalpha():
    except FileNotFoundError:

    return letter_counts
