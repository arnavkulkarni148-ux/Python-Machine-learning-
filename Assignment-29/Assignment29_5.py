import os

def main():
    print("Enter the file name:")
    FileName = input()

    print("Enter the word to count:")
    SearchWord = input()

    Count = 0

    if os.path.exists(FileName):
        fobj = open(FileName, "r")

        for line in fobj:
            words = line.split()

            for word in words:
                if word == SearchWord:
                    Count += 1

        fobj.close()

        print(f"Frequency of {SearchWord} in {FileName} is: {Count}")

    else:
        print("File is not present.")

if __name__ == "__main__":
    main()