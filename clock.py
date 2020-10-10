from apscheduler.schedulers.blocking import BlockingScheduler

import bot
import autofollow

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=60)
def tweet_job():
    bot.main()

@sched.scheduled_job('interval', minutes=60)
def autofollow_job():
    autofollow.main()

sched.start()