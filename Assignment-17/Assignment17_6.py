# Display * pattern

def Display_pattern(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():
    Num = int(input("Enter a number: "))
    Display_pattern(Num)

if __name__ == "__main__":
    main()
