#!/usr/bin/python
# -*- coding: UTF-8 -*-

from email.mime.text import MIMEText
from email.header import Header

# 输入Email地址和口令:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server: ')
# 输入收件人地址:
to_addr = raw_input('To: ')

import smtplib
msg = MIMEText("fjjafjafsjfs", "plain", "utf-8")
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()