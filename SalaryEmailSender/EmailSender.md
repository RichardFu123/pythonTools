# EmailSender.py

> Shawn
> 11/27/2018


用于发送email.

发送email最容易出错的不是程序,而是搞定发送的email邮箱.

发送email的更多知识见: http://www.runoob.com/python3/python3-smtp.html

软件本体见 https://blog.csdn.net/weixin_41084236/article/details/84325652

----

```python
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class EmailSender:
    my_sender = ''  # 发件人邮箱账号
    my_pass = ''  # 发件人邮箱密码
    sender_name = ''  # 发件人邮箱名称

    def __init__(self, sender, pas, name):
        self.my_sender = sender
        self.my_pass = pas
        self.sender_name = name

    def send_mail(self, address, content, to_name, title):
        ret = True
        try:
            msg = MIMEText(content, 'html', 'utf-8')
            msg['From'] = formataddr([self.sender_name, self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr([to_name, address])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = title  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [address, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret
```