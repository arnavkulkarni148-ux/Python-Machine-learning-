#  Display the star pattern

def Display_pattern(No):
    for i in range(No):
        for j in range(No):
            print("*",end=" ")
        print()

def main():
    No = int(input("Enter a number: "))

    Display_pattern(No)

if __name__ == "__main__":
    main() 