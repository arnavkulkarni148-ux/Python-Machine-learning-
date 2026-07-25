import os
import shutil
import schedule
import time
import datetime

def CopyFiles(SourceDir, DestinationDir):

    if not os.path.isdir(SourceDir):
        print("Source Directory does not exist.")
        return

    if not os.path.isdir(DestinationDir):
        print("Destination Directory does not exist.")
        return

    LogFile = open("CopyLog.txt", "a")

    for FolderName, SubFolder, FileNames in os.walk(SourceDir):

        for File in FileNames:

            if File.endswith(".txt"):

                SourcePath = os.path.join(FolderName, File)

                DestinationPath = os.path.join(DestinationDir, File)

                try:
                    shutil.copy(SourcePath, DestinationPath)

                    CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

                    LogFile.write(f"{File} copied successfully at {CurrentTime}\n")

                    print(f"{File} Copied Successfully")

                except Exception as e:

                    LogFile.write(f"Failed to copy {File} : {e}\n")

                    print(f"Unable to copy {File}")

    LogFile.close()

def main():

    SourceDir = input("Enter Source Directory : ")
    DestinationDir = input("Enter Destination Directory : ")

    schedule.every(1).minutes.do(CopyFiles, SourceDir, DestinationDir)

    print("Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()