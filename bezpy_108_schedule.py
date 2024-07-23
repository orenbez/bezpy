# Documentation: https://schedule.readthedocs.io/en/stable
# performs scheduled task without using Windows Task Scheduler
# https://www.geeksforgeeks.org/python-schedule-library/


import schedule  # requires 'pip install schedule'
from time import sleep


def automated_message():
    print('message')


def run_schedule():
    while True:
        schedule.run_pending()  # run all the pending jobs that are scheduled
        sleep(1)


def greet(name: str):
    print('Hello', name)


# schedule.every(interval)
job1 = schedule.every().day.at('06:00').do(automated_message)  # job1 = schedule.every().day.at('06:00').do(automated_message)  #
job2 = schedule.every(15).seconds.do(automated_message)
job3 = schedule.every(3).weeks.do(automated_message)

# pass parameters to the task function
job4 = schedule.every(2).seconds.do(greet, name='Alice')
job5 = schedule.every(4).seconds.do(greet, name='Bob')

schedule.get_jobs()         # returns schedule as list e.g. ...   [..., Every 15 seconds do automated_message() (last run: 2022-05-16 11:43:36, next run: 2022-05-16 11:43:51), ...]
schedule.cancel_job(job3)   # stop a scheduled task from getting executed
schedule.clear()            # remove all the scheduled jobs


# set job6 & job7 with the repeat decorator
@schedule.repeat(schedule.every(3).seconds, "World")
@schedule.repeat(schedule.every(6).seconds, "Mars")
def hello(planet: str):
    print("Hello", planet)


if __name__ == '__main__':
    run_schedule()
