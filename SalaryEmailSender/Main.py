"""
Shawn 11/21/2018
程序主入口
"""

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
