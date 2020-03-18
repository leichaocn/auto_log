"""
用于定时执行整个流程
执行命令：
nohup python3 autorun.py &

"""

from datetime import datetime
from time import sleep
import schedule
import os

def do_job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # your_file改为自己的文件名。
    # 执行
    os.system('jupyter nbconvert --to notebook --execute your_file.ipynb')
    # 转成md格式
    os.system('jupyter nbconvert --to markdown your_file.ipynb')
    # 转pdf，这里result.md是一个预先编辑好的md文件，仅引用到了上面文件执行后的图片路径。
    os.system('pandoc result.md --pdf-engine=xelatex -V mainfont=SimSun -o result.pdf')
    # 发送邮件
    os.system('jupyter nbconvert --to notebook --execute automail.ipynb')



# schedule.every(15).seconds.do(do_job)   # 每15秒
# schedule.every().minutes.do(do_job)   # 每分   
# schedule.every().hour.do(do_job)   # 每小时

schedule.every().day.at("23:35").do(do_job)   # 每天23：30
# schedule.every(5).to(10).days.do(do_job)    # 每5到10天
# schedule.every().wednesday.at("13:15").do(do_job)  # 每周三23:15分
  
while True:
    schedule.run_pending()
    sleep(1)
