import math

number = float(input("Enter a number to use: "))
operation = input("Which operation? sqrt (s), arcsin (a), arccos (c), arctan (t): ")
if operation == 's':
    if number < 0:
        print("Input should be non-negative")
        exit(1)
    print("The square root of the input is\n" + str(math.sqrt(number)))
elif operation == 'a':
    if number < -1 or number > 1:
        print("Input should be between -1 and 1")
        exit(1)
    print("The arcsine of the input is\n" + str(math.asin(number)))
elif operation == 'c':
    if number < -1 or number > 1:
        print("Input should be between -1 and 1")
        exit(1)
    print("The arccosine of the input is\n" + str(math.acos(number)))
elif operation == 't':
    print("The arctangent of the input is\n" + str(math.atan(number)))
else:
    print("Error; the given operation is not valid.\nValid operations are:\ns: sqrt; a: arcsin; c: arccos; t: arctan")
    exit(1)