import os

def main():
    print("Enter the file name:")
    FileName = input()

    print("Enter the word to search:")
    WordFind = input()

    if os.path.exists(FileName):
        fobj = open(FileName, "r")

        Found = False

        for line in fobj:
            words = line.split()

            if WordFind in words:
                Found = True
                break

        fobj.close()

        if Found:
            print(f"{WordFind} is present in {FileName}")
        else:
            print(f"{WordFind} is not present in {FileName}")

    else:
        print("File is not present.")

if __name__ == "__main__":
    main()