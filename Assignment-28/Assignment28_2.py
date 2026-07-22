import os

def main():
    print("Enter a File name : ")
    FileName = input()
    WordsCount = 0

    if os.path.exists(FileName) == True:
        fobj = open(FileName,"r")
        for line in fobj:
            words = line.split()
            WordsCount += len(words)
        fobj.close()
        print(f"Toatl number of words in {FileName} is : {WordsCount}") 
    else:
        print("File is not present")

if __name__ == "__main__":
    main()