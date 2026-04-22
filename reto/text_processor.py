def count_words_chars(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.split()
    num_words = len(words)
    num_chars_with_spaces = len(text)
    num_chars_without_spaces = len(text.replace(' ', ''))
    return num_words, num_chars_with_spaces, num_chars_without_spaces

def replace_word(file_path, old_word, new_word):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    new_text = text.replace(old_word, new_word)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Word replaced successfully.")

def vowel_histogram(file_path):
    import matplotlib.pyplot as plt
    vowels = 'aeiouAEIOU'
    counts = {v: 0 for v in vowels}
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    for char in text:
        if char in vowels:
            counts[char] += 1
    plt.bar(counts.keys(), counts.values())
    plt.title('Vowel Occurrence Histogram')
    plt.xlabel('Vowels')
    plt.ylabel('Count')
    plt.show()