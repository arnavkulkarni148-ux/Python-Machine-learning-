# Display length of name enter by user 

def Display_Length(name):
    count = 0
    for i in name:
        count = count + 1
    return count

def main():
    name = input("Enter a name : ")

    Ret = Display_Length(name)

    print(f"The length of {name} is : {Ret} ")

if __name__ == "__main__":
    main()