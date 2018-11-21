"""
Shawn 11/21/2018
数据类,用于传递reader读取的数据
"""


class OneEmailInfo:
    name = ""
    email_address = ""
    date_str = ""
    manager = ""
    title = ""
    personal_part = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        elements = ''
        for element in self.personal_part:
            elements += str(element)
            elements += " "
        return (
                self.name+" "
                + self.email_address + " "
                + self.date_str + " "
                + self.manager + " "
                + self.title + " "
                + elements
        )
