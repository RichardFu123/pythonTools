# ReadXLSX.py

> Shawn
> 11/23/2018


这个类负责读取excel表格的内容.根据需求就是读取xlsx文件.

这个类实现的是根据关键字确定所需信息区域,.

然后根据读取的每个人的信息分别打包成制作单个邮件所需要的全部数据的数据包

软件本体见 https://blog.csdn.net/weixin_41084236/article/details/84325652

openpyxl相关的知识详见[这里](https://openpyxl.readthedocs.io/en/stable/)

----

```python
import openpyxl
import OneEmailInfo


class ReadXLSX:
    work_book = None
    salary_sheet = None
    address_sheet = None
    sheets = []

    max_row = 0
    max_col = 0
    name_col = 0
    rows_in_salary = None
    cols_in_salary = None
    row_lines_in_salary = []
    col_lines_in_salary = []

    def __init__(self, file_name):
        self.work_book = openpyxl.load_workbook(file_name)  # 读取xlsx文件
        self.sheets = self.work_book.get_sheet_names()  # 获取文件内每张表格的名称

        try:  # 如果已经命名了相应的表单,则按名称指定,否则默认第二张表单为地址表单, 第一张为工资表
            if "邮件地址" in self.sheets and "工资数据" in self.sheets:
                self.address_sheet = self.work_book.get_sheet_by_name("邮件地址")
                self.salary_sheet = self.work_book.get_sheet_by_name("工资数据")
            else:
                self.address_sheet = self.work_book.get_sheet_by_name(self.sheets[1])
                self.salary_sheet = self.work_book.get_sheet_by_name(self.sheets[0])
        except Exception:
            print("Can not get sheets.")

        try:  # 将工资表以行模式和列模式分别读取
            self.rows_in_salary = self.salary_sheet.rows
            for row in self.rows_in_salary:
                self.row_lines_in_salary.append(col.value for col in row)

            self.cols_in_salary = self.salary_sheet.columns
            for col in self.cols_in_salary:
                self.col_lines_in_salary.append(row.value for row in col)
        except Exception:
            print("Can not read the salary table.")

        for i in range(4, len(self.row_lines_in_salary) + 1):   # 用关键词"合计"来寻找最大行数(openpyxl中行列索引都从1开始,而不是0)
            if self.salary_sheet.cell(row=i, column=2).value == "合计":
                self.max_row = i - 1

        for i in range(1, len(self.col_lines_in_salary) + 1):  # 用关键词来寻找最大列数以及姓名列(这部分不同于行数,如果是固定格式可以直接指定,而不是遍历寻找)
            if self.salary_sheet.cell(row=4, column=i).value == "实发\n工资":
                self.max_col = i
            if self.salary_sheet.cell(row=4, column=i).value == "姓名":
                self.name_col = i

    def get_email_address(self, name):  # 为了方便而编写的根据姓名查询email地址的函数.返回值为地址表单中,对应姓名右侧连接的单元格内容.
        flag = False
        for i in self.address_sheet.iter_rows():
            for j in i:
                if flag:
                    return j.value
                if j.value == name:
                    flag = True

    def get_emails_pack(self):  # 这类的主要出口, 返回值为一个由OneEmailInfo类构成的数组,每个OneEmailInfo类打包了对应姓名的地址、个人信息等邮件构成要素.
        pack = []

        for row in self.salary_sheet.iter_rows(min_row=5, max_row=self.max_row, max_col=self.max_col):  # 在个人信息区域逐行读取
            person = []
            for info in row:  # 将个人信息转为字符串保存
                person.append(str(info.value))
            name = person[self.name_col-1]  # 获取姓名
            email_address = self.get_email_address(name)  # 通过姓名获取邮件地址

            date_str = str(self.salary_sheet.cell(row=2, column=15).value)
            title = str(self.salary_sheet.cell(row=1, column=1).value)
            manager = "HR"  # 这三项是构建表格所需要的每次统一变化的内容

            one_email = OneEmailInfo.OneEmailInfo(name)  # 将获取到的信息打包
            one_email.email_address = email_address
            one_email.date_str = date_str
            one_email.manager = manager
            one_email.title = title
            one_email.personal_part = person

            pack.append(one_email)

        return pack

```

由于工资表和地址信息是分离的,所以要分开查询. 
这里偷了个懒,没有用特别严谨的方式去查询email地址.
所以需要保证,每个姓名的右侧单元格填的是email地址,且每个工资表内的人员在地址表中均存在

如果要改进,可以考虑地址表中缺失的状况, 还可以引入正则表达式来确认email地址.