# -*- coding: UTF-8 -*-


import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class Mail(object):

    def __init__(self,recipient='',recipient1='',sender='18811730879@163.com',my_pass='456.caocao'):
        self.recipient = recipient
        self.recipient1 = recipient1
        self.sender = sender
        self.my_pass = my_pass

    def mail_outbox(self):
        toRecipient = self.recipient.split(",")
        msg = MIMEMultipart()
        msg['From'] = Header("InterFace自动化测试HTML,Log <%s>" % "MrLu", 'utf-8')
        msg['To'] = ",".join(toRecipient)
        msg['Subject'] = Header("自动化测试HTML,Log", "utf-8")
        cur_path = os.path.dirname(os.getcwd())
        attachmentPath = cur_path + '\\report\\'
        attachmentPath1 = cur_path + '\\log\\'
        attachmentTemp = os.listdir(attachmentPath)
        attachmentTemp1 = os.listdir(attachmentPath1)
        for i in range(len(attachmentTemp)):
            if str(attachmentTemp[i]).find(".html") != -1:
                attachmentName = attachmentTemp[i]

        for s in range(len(attachmentTemp1)):
            if str(attachmentTemp1[s]).find(".log") != -1:
                attachmentName1 = attachmentTemp1[s]

        bodyContent = "以下是执行后的测试报告：\n   • %s \n • %s" % (attachmentName,attachmentName1)
        msg.attach(MIMEText(bodyContent, "plain", "utf-8"))
        att = MIMEText(open(attachmentPath +attachmentName, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=' + attachmentName
        msg.attach(att)

        try:
            server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的'SMTP'服务器，端口是25
            server.login(self.sender, self.my_pass)
            server.sendmail(self.sender, toRecipient, msg.as_string())
            # 关闭连接
            server.quit()
            print("报告发送成功")
        except smtplib.SMTPException:
            print("报告无法发送")



