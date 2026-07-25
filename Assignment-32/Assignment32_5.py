import os
import schedule
import time
import datetime

def DeleteEmptyFiles(Directory):

    if not os.path.isdir(Directory):
        print("Directory not found.")
        return

    LogFile = open("DeleteLog.txt", "a")

    for FolderName, SubFolder, FileNames in os.walk(Directory):

        for File in FileNames:

            FilePath = os.path.join(FolderName, File)

            try:

                if os.path.getsize(FilePath) == 0:

                    os.remove(FilePath)

                    CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

                    LogFile.write(f"{FilePath} deleted at {CurrentTime}\n")

                    print(f"{File} Deleted")

            except PermissionError:

                print(f"Permission Denied : {File}")

                LogFile.write(f"Permission Denied : {FilePath}\n")

    LogFile.close()

def main():

    Directory = input("Enter Directory : ")

    schedule.every(1).hours.do(DeleteEmptyFiles, Directory)

    print("Scheduler Started...")

    while True:

        schedule.run_pending()

        time.sleep(1)

if __name__ == "__main__":
    main()