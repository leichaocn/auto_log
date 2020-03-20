"""
用于定时执行整个流程
执行命令：
nohup python3 autorun.py &

"""
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from datetime import datetime
from time import sleep
import schedule
import os


def send_mail():
    date_now = datetime.now().strftime('%Y%m%d')

    # 邮件服务器
    mail_server = 'smtp.163.com'
    mail_server_port = 25

    # 发件人邮箱地址
    from_addr = 'leichaocn@163.com'
    # 发件人邮箱密码
    from_pwd="XXXX"


    # to_addr = 'leichao5@jd.com'
    # to_addrs = ['leichao5@jd.com',
    #             '275072373@qq.com']

    # 收件人邮箱地址
    to_addrs = ["leichao <leichao5@jd.com>",
                "heihei <275072373@qq.com>",]

    # 标题文本
    subjcet ='{}平台简报.pdf'.format(date_now)
    # 正文文本
    text = "完整简报见附件"

    # 对要上传的附件进行文件重命名
    file_one = "result.pdf" 
    file_two = '{}_daily_report.pdf'.format(date_now)
    if os.path.exists(file_two):
        pass
    else:
        os.rename(file_one, file_two)
    # os.remove(file_two)

    ms = MIMEMultipart()
    # ms["To"] = to_addr
    ms["To"] = ",".join(to_addrs)
    ms["From"] = from_addr
    ms["Subject"] = subjcet
    msText = MIMEText(text)
    ms.attach(msText)

    # 上传附件
    fp = open(file_two,'rb') 
    x = fp.read() 
    fp.close() 
    fileMsg = email.mime.base.MIMEBase('application','pdf') 
    fileMsg.set_payload(x) 
    email.encoders.encode_base64(fileMsg) 
    # fileMsg.add_header('Content-Disposition','attachment;filename=one_day_simple_report.pdf') 
    fileMsg.add_header('Content-Disposition','attachment;filename='+file_two) 
    ms.attach(fileMsg)

    # 发送邮件
    mail = smtplib.SMTP(mail_server, mail_server_port)
    mail.starttls()
    mail.login(from_addr, from_pwd)
    mail.sendmail(from_addr, to_addrs, ms.as_string())
    mail.quit()

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
    send_mail()

# schedule.every(15).seconds.do(do_job)   # 每15秒
# schedule.every().minutes.do(do_job)   # 每分   
# schedule.every().hour.do(do_job)   # 每小时

schedule.every().day.at("23:35").do(do_job)   # 每天23：30
# schedule.every(5).to(10).days.do(do_job)    # 每5到10天
# schedule.every().wednesday.at("13:15").do(do_job)  # 每周三23:15分
  
while True:
    schedule.run_pending()
    sleep(1)
