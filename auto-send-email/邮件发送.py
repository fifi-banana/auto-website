# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:31:25 2020

@author: Lenovo
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'ixxx@qq.com'
receivers = '1xxs@qq.com'

message = MIMEText('python邮件发送测试','plain','utf-8')
message['From'] = Header("feifei",'utf-8')
message['To'] = Header("test",'utf-8')

subject = 'Python SMTP邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error:无法发送邮件")    
