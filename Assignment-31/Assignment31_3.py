import os
import schedule
import time
import datetime

def DirectoryCount(DirectoryName):
    Subcount = 0
    fcount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        Subcount += len(SubFolder)
        fcount += len(FileName)

    print("*" * 40)
    print(f"Directory Name : {DirectoryName}")
    print(f"Number of Files : {fcount}")
    print(f"Number of Subdirectories : {Subcount}")
    print(f"Scan Time : {datetime.datetime.now()}")
    print("*" * 40)

def main():
    print("Enter a Directory name : ")
    DirectoryName = input()

    desktop_folder = os.path.join(os.path.expanduser("~"),"Desktop",DirectoryName)

    if os.path.isdir(desktop_folder):
        schedule.every(1).minutes.do(DirectoryCount,desktop_folder)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Directory is not present")

if __name__ == "__main__":
    main()