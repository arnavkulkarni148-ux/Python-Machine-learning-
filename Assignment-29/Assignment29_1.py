import os

def main():
    print("Enter a file name: ")
    FileName = input()

    Ret = os.path.exists(FileName)

    if Ret == True:
        print("File is present in the current directory...")
    else:
        print("File is not present in the current directory... ")


if __name__ == "__main__":
    main()