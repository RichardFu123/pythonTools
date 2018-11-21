# 工资条邮件发送软件 v1.0

> 作者: Shawn

> Python 3.7

* Main.py为程序主入口
* 本软件用于读取符合test.xlsx的工资表表格文件,并将读取的工资条通过邮箱发送.
* 发送的邮件为html格式, 这部分在TableMaker.py
* 发送的邮件通过smtp,默认为qq邮箱,这部分在EmailSender.py
* 表格读取在ReadXLSX.py, 有三项自定义设定在ReadXLSX类的get_emails_pack()下
* OneEmailInfo.py为数据类,用来传递ReadXLSX读取的数据.