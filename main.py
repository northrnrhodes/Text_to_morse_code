morse_dict = {
    "A": ".-", "B": "-...", "C":"-.-.", "D": "-..", "E": ".",  "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--." , "Q": "--.-" , "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
    "X": "-..-", "Y": "-.--", "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": " "}


def convert_morse(text):
    morse_code = []

    for char in text.upper():
        if char in morse_dict:
             morse_code.append(morse_dict[char])

        else:
            morse_code.append("?")


    return print(" ".join(morse_code))

while True:
    text = input("What is your message? \n")
    if text[0].isalpha():
        convert_morse(text)


    else:
        text = text.split(" ")
        print(text)










print(morse_dict.get_items())
