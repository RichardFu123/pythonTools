# Main.py

> Shawn
> 11/28/2018


这部分就是软件的主体.

将Reader和Sender实例. 之后将Reader获取到的每一份数据用TableMaker包装, 用Sender发送.

软件本体见 https://blog.csdn.net/weixin_41084236/article/details/84325652

----

```python
import EmailSender
import ReadXLSX
import TableMaker


if __name__ == "__main__":
    sender = EmailSender.EmailSender("123321@qq.com", "password", "Shawn")
    reader = ReadXLSX.ReadXLSX("test.xlsx")
    info_pack = reader.get_emails_pack()

    for one in info_pack:
        content = TableMaker.TableMaker.pack_up(
            one.name,
            one.title,
            one.manager,
            one.date_str,
            one.personal_part
        )
        status = sender.send_mail(
            one.email_address,
            content,
            one.name,
            one.title)
        if status:
            print(f"{one.name} successful")
        else:
            print(f"{one.name} failed")

```