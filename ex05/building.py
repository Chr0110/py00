import sys
import string

def main():
    """
    this main function mission is to count and return the number of the upper letters, the lower letters, digits, and the spaces in the input string
    """
    if (len(sys.argv) == 1):
        arg = input("What is the text to count?")
    else :
        arg = sys.argv[1]
    upper = 0
    lower = 0
    space = 0
    digits = 0
    letters = 0
    mark = 0
    for i in arg:
        if i.isupper():
            upper += 1
            letters += 1
        elif i.islower():
            lower += 1
            letters += 1
        elif i in string.punctuation:
            mark += 1
            letters += 1
        elif i.isspace():
            space += 1
            letters += 1
        elif i.isdigit():
            digits += 1
            letters += 1
    print(f"The text contains {letters} chatracters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{mark} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")
if __name__ == "__main__":
    main()