import os
import schedule
import time

def DisplayFile(FileName):

    if os.path.exists(FileName):
        try:
            fobj = open(FileName, "r")

            Data = fobj.read()

            if len(Data) == 0:
                print("File is empty.")
            else:
                print("\nContents of File\n")
                print(Data)

            fobj.close()

        except PermissionError:
            print("Permission Denied.")

        except OSError:
            print("File cannot be opened.")
    else:
        print("File does not exist.")

def main():

    FileName = input("Enter File Name : ")

    schedule.every(1).minutes.do(DisplayFile, FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()