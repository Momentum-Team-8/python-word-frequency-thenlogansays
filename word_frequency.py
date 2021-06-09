STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

file = open('praise_song_for_the_day.txt')
file

for i in range(8):
    print(repr(praise.readline()))

def clean_text(file):
    """given text returns text all lowercase, no punctuation, and removes all stop words"""
    text = praise.lower


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
