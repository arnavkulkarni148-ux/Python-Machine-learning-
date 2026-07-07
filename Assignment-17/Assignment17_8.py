# Display pattern of number

def Display_Number(No):
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def main():
    Num = int(input("Enter a number : "))
    Display_Number(Num)

if __name__ == "__main__":
    main()
