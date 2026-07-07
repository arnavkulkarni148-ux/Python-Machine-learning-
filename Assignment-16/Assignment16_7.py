#  Returning True if number is divisible by 5 else False

def Chk_Divisible(no):
    if no % 5 == 0:
        return True
    else:
        return False
    

def main():
    no = int(input("Enter a number: "))
    Ret = Chk_Divisible(no)
    print(Ret)

if __name__ == "__main__":
    main()