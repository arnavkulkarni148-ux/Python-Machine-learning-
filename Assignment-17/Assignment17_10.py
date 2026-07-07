# Additon of digits of number 

def Adddition_number(No):
    sum = 0
    No1 = No
    while(No1 > 0):
        No2 = 0
        No2 = No1 % 10
        sum = sum + No2
        No1 = No1 // 10
    return sum


def main():
    Num = int(input("Enter a number: "))
    Ret = Adddition_number(Num)

    print(f"The Addition of {Num} is {Ret}")

if __name__ == "__main__":
    main()
