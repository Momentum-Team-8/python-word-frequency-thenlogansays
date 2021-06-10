import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    file = open('one-today.txt', 'r')
    text = file.read().lower().split()
    #print(text)

    #all_letters = "abcdefghijklmopqrstuvwxyz"
    #text_to_keep = []

    for char in text:
        table = char.maketrans( "", "", string.punctuation)
        char.translate(table)
    #print(text)

    count_dict = {}

    for word in text:
        
        if word in STOP_WORDS:
            text.remove(word)
        elif word in count_dict:
            count_dict[word] = count_dict[word] +1
        elif word not in count_dict:
            count_dict[word] = 1
    
    file.close()
    print(count_dict)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
