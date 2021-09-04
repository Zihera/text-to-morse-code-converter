morse_code_dict = {'a': '•-', 'b': '-•••', 'c': '-•-•', 'd': '-••', 'e': '•', 'f': '••-•', 'g': '--•', 'h': '••••',
                   'i': '••', 'j': '•---', 'k': '-•-', 'l': '•-••', 'm': '--', 'n': '-•', 'o': '---', 'p': '•--•',
                   'q': '--•-', 'r': '•-•', 's': '•••', 't': '-', 'u': '••-', 'v': '•••-', 'w': '•--', 'x': '-••-',
                   'y': '-•--', 'z': '--••', '1': '•----', '2': '••---', '3': '•••--', '4': '••••-', '5': '•••••',
                   '6': '-••••', '7': '--•••', '8': '---••', '9': '----•', '0': '-----'}


def morse_converter(start_text):
    """Input a string of text, returns the corresponding morse code"""

    output = ""

    for letter in start_text:
        if letter in morse_code_dict:
            changed_text = morse_code_dict[letter] + " "
            output += changed_text
        elif letter == " ":
            space = "/ "
            output += space
        else:
            continue

    return print(output)


if __name__ == '__main__':
    text_to_convert = input("Input text to convert here: ").lower().strip()
    morse_converter(start_text=text_to_convert)
