import psutil
import os
import sys
import time
import smtplib
from email.message import EmailMessage


def DisplayProcess(LogFileName):
    try:
        with open(LogFileName, "w") as fobj:

            fobj.write("-" * 50 + "\n")
            fobj.write("Information of Running Processes\n")
            fobj.write("-" * 50 + "\n\n")

            for process in psutil.process_iter(["pid", "name", "username"]):

                try:
                    info = process.info

                    fobj.write(f"Process Name : {info['name']}\n")
                    fobj.write(f"PID          : {info['pid']}\n")
                    fobj.write(f"Username     : {info['username']}\n")
                    fobj.write("-" * 50 + "\n")

                except (psutil.NoSuchProcess,
                        psutil.AccessDenied,
                        psutil.ZombieProcess):
                    pass

    except Exception as e:
        print("Unable to create log file:", e)


def CreateLogFile(DirectoryName):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = "Marvellous_%s.log" % timestamp

    LogFile = os.path.join(DirectoryName, FileName)

    DisplayProcess(LogFile)

    print("Log File Created Successfully")

    return LogFile


def DirectoryCheck(FolderName):

    if os.path.exists(FolderName):

        if not os.path.isdir(FolderName):
            print("Given path exists but it is not a directory.")
            return None

    else:
        os.mkdir(FolderName)
        print("Directory created successfully.")

    return CreateLogFile(FolderName)


def SendMail(FileName, ReceiverMail):

    SenderMail = "arnav@gmail.com"

    Password = "**** **** **** ****"

    try:

        msg = EmailMessage()

        msg["Subject"] = "Running Process Log"

        msg["From"] = SenderMail

        msg["To"] = ReceiverMail

        msg.set_content(
            "Hello,\n\nPlease find the attached running process log file.\n\nThank You."
        )

        with open(FileName, "rb") as f:
            FileData = f.read()

        msg.add_attachment(
            FileData,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(FileName)
        )

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(SenderMail, Password)

        server.send_message(msg)

        server.quit()

        print("Mail sent successfully.")

    except Exception as e:
        print("Unable to send mail.")
        print("Error:", e)


def main():

    if len(sys.argv) != 3:
        print("Invalid command input...")
        print("give command as : python ProcInfoLog.py <DirectoryName> <ReceiverEmail>")
        return

    DirectoryName = sys.argv[1]

    ReceiverMail = sys.argv[2]

    LogFile = DirectoryCheck(DirectoryName)

    if LogFile != None:
        SendMail(LogFile, ReceiverMail)


if __name__ == "__main__":
    main()