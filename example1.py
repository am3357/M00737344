value = input('''options listed below:,
              \t 1. Roll
              \t 2. sweep
              \t 3. Scroll
              Type the number of your choice and press enter.''')

def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val

while True:
    if value.isdigit() == True: #.isdigit()
        value = int(value)
        if value > 3 or value < 1:
            value = input("please put a number between 1 and 3.")
            continue
        else:
            break #on correct value datatype: exit the loop
    else:
        value= input("invalid input, please provide an integer:")

#print("the converted value is:",value)
#print(f'it is of type {type(value)}.')

if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))
