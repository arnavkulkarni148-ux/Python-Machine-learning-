# Create three thread small capital and digit 

import threading

def SmallChar(value):
    count = 0
    for char in value:
        if char.islower():
            count = count + 1

    print("Count of Lowercase charcters are:",count)
    print("Thread Name is:",threading.current_thread().name)
    print("Thread Id of Smaller is:",threading.get_ident())

def CapitalChar(value):
    count = 0
    for char in value:
        if char.isupper():
            count = count + 1

    print("Count of uppercase charcters are:",count)
    print("Thread Name is:",threading.current_thread().name)
    print("Thread Id of Capital is:",threading.get_ident())

def Digit(value):
    count = 0
    for char in value:
        if char.isdigit():
            count = count + 1
    print("Count of digit is:",count)
    print("Thread Name is:",threading.current_thread().name)
    print("Thread Id of Digit is:",threading.get_ident())

def main():

    value = input("Enter value: ")

    Small = threading.Thread(target=SmallChar,args=(value,))
    Capital = threading.Thread(target=CapitalChar,args=(value,))
    Digits = threading.Thread(target=Digit,args=(value,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()
    
if __name__ == "__main__":
    main()
