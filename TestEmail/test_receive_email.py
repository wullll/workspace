#!/usr/lib/python3
# -*-coding:utf-8-*-

"""
接收邮件
"""
import poplib

# 输入邮件地址，口令和pop3服务器地址 ：
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr

email = "wuliangliang160@163.com"
password = "211211"
pop3_server = "pop.163.com"


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# indent用于缩进显示：
def print_info(msg, indent=0):
    file = open('myEmail.html', 'w+')
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print("%s%s: %s" % (' ' * indent, header, value))
            file.write(' ' * indent + header + value)
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print("%spart %s" % (' ' * indent, n))
            file.write(' ' * indent + str(n))
            print('%s--------------' % (' ' * indent))
            file.write(' ' * indent)
            print_info(part, indent+1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % (' ' * indent, content+'...'))
            file.write(' ' * indent + content + '...')
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))
            file.write(' ' * indent + content_type)


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def test_accept_email():
    # 连接到服务器
    server = poplib.POP3(pop3_server)
    # 打开或关闭调试信息
    server.set_debuglevel(1)
    # 打印pop服务器欢迎文字
    print(server.getwelcome().decode('utf-8'))
    # 身份认证
    server.user(email)
    server.pass_(password)
    # stat() 返回邮件数量和占用空间
    print("Message : %s , Size: %s" % server.stat())
    # list()返回所有邮件数量
    resp, mails, octets = server.list()
    print(resp, mails, octets)
    # 获取最新的一封邮件,索引从1开始
    index = len(mails)
    resp, lines, octets = server.retr(index)
    # lines存放了邮件的原始文本的每一行
    # 可以获得整个邮件的原始文本：
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件
    msg = Parser().parsestr(msg_content)
    print(msg)
    print_info(msg, 2)
    server.quit()


if __name__ == "__main__":
    test_accept_email()


