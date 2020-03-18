# 自动日志生成
## 各文件说明
### 1.your_file.ipynb，
你的日志统计主要代码，确保可以运行。该文件的作用是生成每天的统计图表。
### 2.你的日志文件result.md
你的日志文件，该文件用于提供文本格式，通过引用文件路径，自动导入统计图表。
### 3.automail.py
邮件发送代码，该文件可设置发件然、收件人等。
### 4.autorun.py
全流程执行代码，该文件用于定时执行整个流程。
## 使用方法
### 1.编辑文件
调试你的your_file.ipynb，result.md，配置你的automail.py、autorun.py
### 2.执行命令
    nohup python3 autorun.py &