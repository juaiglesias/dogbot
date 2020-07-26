from apscheduler.schedulers.blocking import BlockingScheduler

import bot

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=60)
def timed_job():
    bot.main()

sched.start()