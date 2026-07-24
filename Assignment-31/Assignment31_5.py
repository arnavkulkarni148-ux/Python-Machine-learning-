import os
import schedule
import time
import datetime

def DirectoryCount(DirectoryPath):

    Count = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        Count += len(FileName)

    fobj = open("DirectoryCountLog.txt", "a")

    CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj.write(f"Directory : {DirectoryPath}\n")
    fobj.write(f"Number of Files : {Count}\n")
    fobj.write(f"Date and Time : {CurrentTime}\n")
    fobj.write("-" * 40 + "\n")

    fobj.close()

    print("Log Updated Successfully.")

def main():

    DirectoryPath = input("Enter directory path : ")

    if os.path.isdir(DirectoryPath):

        schedule.every(5).minutes.do(DirectoryCount, DirectoryPath)

        print("Scheduler Started...")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Directory not found.")

if __name__ == "__main__":
    main()