import schedule
import time

def LunchReminder():
    print("Lunch Time!")

def WorkOver():
    print("Wrap up work!")


def main():
    schedule.every().day.at("13:00").do(LunchReminder)
    schedule.every().day.at("18:00").do(WorkOver)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()