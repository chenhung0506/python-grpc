import log as logpy
import sys
import traceback
import const
import os
from threading import Timer,Thread,Event
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.header import Header

log = logpy.logging.getLogger(__name__)

def is_valid_date(date_string):
    if date_string:
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    return False

def except_raise(e):
    error_class = e.__class__.__name__ #取得錯誤類型
    detail = e.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
    #print(tb)
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    funcName = lastCallStack[2] #取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    return errMsg

sched = BackgroundScheduler()

def prepare_batch_blocking(job,args):
    # sched.shutdown()
    # sched.add_job(job, 'interval', seconds=int(const.FREQUENCE), args=(args,))
    sched.add_job(job, CronTrigger.from_crontab(const.TRANSMIT_CRON))
    sched.start()
    return "Start scheduler id: " + str(sched.get_jobs())

def stop_batch():
    sched.remove_all_jobs()
    # sched.remove_all_jobs(jobstore=None)
    # sched.shutdown()
    return "Stop scheduler id: " + str(sched.get_jobs())

def prepare_batch_background(job,cronStr):
    sched.add_job(job, CronTrigger.from_crontab(cronStr))
    try: 
        sched.start()
    except Exception as e:
        log.info(e)
    return "Start scheduler id: " + str(sched.get_jobs())

def setLogFileName():
    try:
        if not os.path.exists(const.LOG_FOLDER_PATH):
            os.makedirs(const.LOG_FOLDER_PATH)
    except OSError as e:
        print(e)
    conf={}
    conf['name'] = datetime.today().strftime('%Y-%m-%d') + '-log.log'
    conf['verbose'] = const.LOG_LEVEL
    conf['log_path'] = const.LOG_FOLDER_PATH 
    conf['log_file'] = conf['log_path'] + conf['name']
    logpy.setup_logging(conf)
    log.info("change log file name to:" + conf['name'])
