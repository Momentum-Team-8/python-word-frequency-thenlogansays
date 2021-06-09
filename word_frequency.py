STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

today = "one-today.txt"
praise = "praise_song_for_the_day.txt"
hill = "the-hill-we-climb.txt"

def readfile(praise):
    """given a file opens and reads file"""
    file = open(praise)

for i in range(8):
    print(repr(file.readline()))

def clean_text(file):
    """given text returns text all lowercase, no punctuation, and removes all stop words"""
    text = file.lower
    all_letters = "abcdefghijklmopqrstuvwxyz"
    text_to_keep = ""
    for char in text:
        if char in all_letters:
            text_to_keep += char
    return text_to_keep


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    readfile()

    pass




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
