import sys
from stats import count_words

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def text_file():
    with open(sys.argv[1]) as f:
        file_content = f.read()
    return file_content

# function that count the number of characters in a text in a dictionary -> {a: 1, b: 2, c: 3}
# consider a to z only
def count_characters(text):
    characters = {}
    for char in text.lower():
        if 'a' <= char <= 'z':
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def main ():
    # clean the terminal
    print('\033c')
    text = text_file()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f'Found {count_words(text)} total words')
    print("----------- Character Count -----")
    for key, value in count_characters(text).items():
        print(f'{key}: {value}')
    print('============= END ===============')

if __name__ == '__main__':
    main()