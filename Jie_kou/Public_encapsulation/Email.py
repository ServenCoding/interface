# -*- coding: UTF-8 -*-


import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def mail(recipient=''):
    sender = '18811730879@163.com'
    my_pass = '*********'
    toRecipient = recipient.split(",")

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    msg['From'] = Header("API自动化测试报告 <%s>" % "MrLu", 'utf-8')  # 显示的发件人
    msg['To'] = ",".join(toRecipient)
    msg['Subject'] = Header("自动化测试报告", "utf-8")  # 邮件主题

    # 附件名字与路径
    cur_path = os.path.dirname(os.getcwd())
    timeStr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    attachmentPath = cur_path + '\\report\\'

    attachmentTemp = os.listdir(attachmentPath)
    for i in range(len(attachmentTemp)):
        if str(attachmentTemp[i]).find(".html") != -1:
            attachmentName = attachmentTemp[i]

    # 邮件正文内容
    bodyContent = "以下是执行后的测试报告：\n   • %s" % attachmentName
    msg.attach(MIMEText(bodyContent, "plain", "utf-8"))

    # 构建附件，发送当前目录下的HTML测试报告文件
    att = MIMEText(open(attachmentPath + attachmentName, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=' + attachmentName
    msg.attach(att)
    try:
        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的'SMTP'服务器，端口是25
        server.login(sender, my_pass)

        server.sendmail(sender, toRecipient, msg.as_string())
        # 关闭连接
        server.quit()
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("无法发送邮件")



