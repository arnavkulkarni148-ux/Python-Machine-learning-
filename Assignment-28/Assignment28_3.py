import os 

def main():
    print("Enter a file name : ")
    FileName = input()

    Ret = os.path.exists(FileName)

    if Ret == True:
        fobj = open(FileName)
        print(f"Each line from the file {FileName}: ")
        for lines in fobj:
            print(lines)
    else:
        print("File is not present")


if __name__ == "__main__":
    main()