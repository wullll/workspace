#!/usr/lib/python3
# -*-coding:utf-8-*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
image_path = 'image.png'
# from_addr = "wuliangliang160@163.com"
# password = "211211"
# to_addr = "yongyuanaiwan@126.com"   # "763889328@qq.com"
# smtp_server = "smtp.163.com"


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def _send_email():
    from_addr = "wuliangliang160@163.com"
    password = "211211"
    to_addr = "2114808211@qq.com"  # "763889328@qq.com"
    smtp_server = "smtp.163.com"
    msg = MIMEMultipart()
    msg.attach(MIMEText('遥远的距离', 'plain', 'utf-8'))
    msg['From'] = _format_addr('发件人 <%s>' % from_addr)
    msg['To'] = _format_addr('收件人 <%s>' % to_addr)
    msg['Subject'] = Header('标题', 'UTF-8').encode()
    file = open('test.txt', 'rb')
    att1 = MIMEText(file.read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    msg.attach(att1)

    # 邮件服务器默认端口25
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password=password)
    server.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())
    server.quit()


# 发送邮件附件
def send_email_file():
    from_addr = "wuliangliang160@163.com"
    password = "211211"
    to_addr = "cst1992@126.com"
    # to_addr = "2114808211@qq.com"
    smtp_server = "smtp.163.com"
    # 邮箱设置
    text = "con   恭喜你获得苏宁的offer，祝福你工作顺利，早日事业有成。重复三次，三次结果是否一致？"
    msg = MIMEMultipart()
    msg.attach(MIMEText(text, 'plain', 'utf-8'))
    msg['From'] = _format_addr('我 <%s>' % from_addr)
    msg['To'] = _format_addr('你 <%s>' % to_addr)
    msg['Subject'] = Header('题目', 'UTF-8').encode()
    # 添加邮件正文 MIMEText
    # msg.attach(MIMEText(text, 'plain', 'utf-8'))
    # 添加附件 MIMEBase对象  试试ppt
    #
    with open('image.png', 'rb') as f:
        mime = MIMEBase('image', 'png', filename='test.png')
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        # base64编码
        encoders.encode_base64(mime)
        msg.attach(mime)

    f = open('test.pptx', 'rb')
    att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="test.pptx"'
    msg.attach(att1)
    f.close()
    # 邮件服务器默认端口25
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password=password)
    print(from_addr, to_addr)
    print("邮件正文是：..", msg.as_string())
    # for i in range(10):
    server.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())
    server.quit()


if __name__ == '__main__':
    # _send_email()
    # for i in range(3):
    #     threading.Thread(target=send_email_file).start()
    send_email_file()

