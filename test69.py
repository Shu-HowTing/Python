# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
利用python发送邮件
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送方邮箱
sender   = '15262691505@163.com'
# 接受方邮箱
receiver = '1549189937@qq.com'
# 邮件主题
subject  = 'python email'
# smtp服务器 ，Email服务提供商服务器地址
smtpserver = 'smtp.163.com'
# 发送者用户名
username = '15262691505@163.com'
# 是授权密码，而不是登录密码!!!
password = '1234qwer'

# 传入'plain'表示纯文本,中文需参数‘utf-8’，单字节字符不需要
msg = MIMEText('This is an email from python!', 'plain', 'utf-8')
msg['Subject'] =  Header(subject, 'utf-8')
msg['From']    =  'Ding<15262691505@163.com>'
msg['To']      =  '1549189937@qq.com'
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()