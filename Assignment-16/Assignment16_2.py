#  Checking odd or even number using ChkNum()

def ChkNum(no):
    if no % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    no = int(input("Enter a number : "))
    Ret = ChkNum(no)
    print(Ret)

if __name__ == "__main__":
    main()