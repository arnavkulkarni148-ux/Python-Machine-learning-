# Checking Whether the given number is positive, negative or zero

def Chk_Number(no):
    if no == 0:
        return "Zero"
    elif no > 0:
        return "Positive Number"
    else:
        return "Negative Number"
    

def main():
    no = int(input("Enter a number : "))
    Ret = Chk_Number(no)
    print(Ret)

if __name__ == "__main__":
    main()