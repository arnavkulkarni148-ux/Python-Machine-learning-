import os
import shutil
import schedule
import time
import datetime

def BackupFile(SourceFile, DestinationDir):

    if not os.path.exists(SourceFile):
        print("Source file does not exist.")
        return

    if not os.path.exists(DestinationDir):
        print("Destination directory does not exist.")
        return

    FileName = os.path.basename(SourceFile)

    CurrentTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    Name, Extension = os.path.splitext(FileName)

    BackupFileName = f"{Name}_{CurrentTime}{Extension}"

    DestinationPath = os.path.join(DestinationDir, BackupFileName)

    shutil.copy(SourceFile, DestinationPath)

    with open("backup_log.txt", "a") as fobj:
        LogTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        fobj.write(f"Backup completed successfully at {LogTime}\n")

    print("Backup completed successfully.")

def main():

    SourceFile = input("Enter source file path: ")
    DestinationDir = input("Enter destination directory path: ")

    schedule.every(1).hours.do(BackupFile, SourceFile, DestinationDir)

    print("Backup Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()