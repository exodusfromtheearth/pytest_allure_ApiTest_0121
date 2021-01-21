# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:sendEmail.py
# Time:2021/1/20 8:13 下午

"""
封装发送邮件的方法

"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(report_file, pytestconfig):
    msg = MIMEMultipart()   # 读取html文件内容
    f = open(report_file, 'rb')
    mail_body = f.read()
    f.close()
    # stress_body = Consts.STRESS_LIST
    # result_body = Consts.RESULT_LIST
    # body2 = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (stress_body, result_body)
    message = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    msg['Subject'] = Header("接口自动化测试报告"+"_"+tm, 'utf-8')
    msg['From'] = pytestconfig.getini('sender')
    receivers = pytestconfig.getini('receiver')
    toclause = receivers.split(',')
    msg['To'] = ",".join(toclause)

    msg.attach(message)

    try:
        smtp163 = smtplib.SMTP()
        smtp163.connect(pytestconfig.getini('smtp_server'), port=pytestconfig.getini('port'))
        smtp163.login(pytestconfig.getini('sender'), pytestconfig.getini('emailpsw'))
        smtp163.sendmail(pytestconfig.getini('sender'), toclause, msg.as_string())
    except Exception as e:
        print(e)
        print("发送失败")

    else:
        print("发送成功")
    finally:
        smtp163.quit()


