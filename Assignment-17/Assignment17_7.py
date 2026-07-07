# Display pattern of number 

def Display_pattern(No):
    for i in range(1,No+1):
        for i in range(1,No+1):
            print(i,end=" ")
        print()

def main():
    Num = int(input("Enter a number: "))
    Display_pattern(Num)

if __name__ == "__main__":
    main()