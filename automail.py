"""
发送邮件程序，先用ipynb格式，方便调试。
命令行执行命令：
python3 automail.py

"""

import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from datetime import datetime
date_now = datetime.now().strftime('%Y%m%d')

# 邮件服务器
mail_server = 'smtp.163.com'
mail_server_port = 25


# 发件人，即你的邮箱地址
from_addr = 'leichaocn@163.com'
# 你的邮箱密码
from_pwd="XXXX"


# to_addr = 'leichao5@jd.com'
# to_addrs = ['leichao5@jd.com',
#             '275072373@qq.com']

# 收件人
to_addrs = ["leichao <leichao5@jd.com>",
            "heihei <275072373@qq.com>",]


subjcet ='{}平台简报.pdf'.format(date_now)
text = "完整简报见附件"


ms = MIMEMultipart()
# ms["to"] = to_addr
ms["To"] = ",".join(to_addrs)
# ms["To"] = to_addr
ms["From"] = from_addr
ms["Subject"] = subjcet
msText = MIMEText(text)
ms.attach(msText)

# 对要上传的附件进行文件重命名
file_one = "one_day_simple_report.pdf" 
file_two = '{}_daily_report.pdf'.format(date_now)
if os.path.exists(file_two):
    pass
else:
    os.rename(file_one, file_two)
# os.remove(file_two)


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
