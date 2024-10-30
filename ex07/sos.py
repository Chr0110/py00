import sys
import string
def is_alphanumeric(char):
    if (char == " "):
        return 1
    return char.isalnum()
def morse(arg:any) -> string:
    result = []
    morse_code_map = {
    " ": "/ ", 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'}
    for c in arg.upper():
        result.append(morse_code_map[c])
    return ' '.join(result)
def main():
    """
    this program here accept the check the input (arg) to check if it's valid to convert it to a morse word, only the alphanumeric characters are accepted
    """
    lenght = len(sys.argv)
    if (lenght == 1 or lenght > 2):
        exit(1)
    arg = sys.argv[1]
    error = 0
    for x in range(len(arg)):
        if (is_alphanumeric(arg[x]) == 0):
            print("AssertionError: the arguments are bad")
            sys.exit(1)
    print(morse(arg))

if __name__ == "__main__":
    main()