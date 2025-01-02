def text_file():
    with open('./books/frankenstein.txt') as f:
        file_content = f.read()
    return file_content

# funtion that count the number of works in a text
def count_words(text):
    words = text.split()
    return len(words)

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
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'Number of words: {count_words(text)}\n')
    for key, value in count_characters(text).items():
        print(f'{key}: character was found {value} times')
    print('--- End report ---')

if __name__ == '__main__':
    main()