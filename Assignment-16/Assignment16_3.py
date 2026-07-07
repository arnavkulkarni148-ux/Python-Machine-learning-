# Addition of two numbers using Add()
def Add(No1,No2):
    Ans = No1 + No2
    return Ans

def main():
    No1 = int(input("Enter a first number: "))
    No2 = int(input("Enter a second Number: "))

    Ret = Add(No1,No2)

    print(f"Addition of {No1} + {No2} is : {Ret}")
if __name__ == "__main__":
    main()