import sys
lenght = len(sys.argv)
x = 1;
if (lenght == 1):
    sys.exit(1)
while x < lenght :
    try:
        int(sys.argv[x])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    x = x+1;
if lenght > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
arg = int(sys.argv[1])
if arg % 2 == 0:
    print("I'm Even")
    sys.exit(1)
else:
    print("I'm Odd")
    sys.exit(1)