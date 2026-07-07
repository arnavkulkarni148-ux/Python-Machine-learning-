# Printing * on screen

def Print_Star(no):
    for i in range(no):
        print("*" " ",end = "")
        if i == 1:
            print(end=" ") 

def main():
    no = int(input("Enter how many stars do you want(*) : "))
    Print_Star(no)

if __name__ == "__main__":
    main()

    #  I want output as * *  * * * for 5 