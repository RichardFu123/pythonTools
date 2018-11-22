"""
Shawn 11/21/2018
制表部分, 将要发送的邮件内容转换成html格式
"""


class TableMaker:
    @staticmethod
    def table(s):  # 表格总包装
        return "<table border=\"1px\">" + s + "</table>"

    @staticmethod
    def tr(s):  # 表格行包装
        return "<tr>" + s + "</tr>"

    @staticmethod
    def td_spin(s, span):  # 表格跨列单元格包装
        return f"<td colspan={span}>" + s + "</td>"

    @staticmethod
    def td(s):  # 表格普通单元格包装
        return "<td>" + s + "</td>"

    @staticmethod
    def p(s):  # 段落包装
        return "<p>" + s + "</p>"

    @staticmethod
    def salary_str(row_line_array):  # 个人数据包装, 将数组包装成表格的一行
        info = ""
        for element in row_line_array:
            info += TableMaker.td(element)
        return TableMaker.tr(info)

    @staticmethod
    def table_head_str(date_str, title):  # 表头包装, 根据输入的标题、日期输出四行固定格式的表头
        line3data = [
            "部门", "姓名", "卡号", "开户行", "入职日期",
            "基本工资", "岗位工资", "合计", "绩效", "工资合计",
            "实际天数", "出勤天数", "缺勤天数", "病假天数", "缺勤",
            "绩效","其他", "合计", "午贴", "交补",
            "其它", "合计", "应发工资", "公司社保", "公司公积金",
            "合计", "个人社保", "个人公积金", "其它", "合计",
            "税前工资", "个税1", "个税2", "实发工资"
        ]

        line0 = TableMaker.tr(TableMaker.td_spin(title, 34))
        line1 = TableMaker.tr(
            TableMaker.td_spin("编制单位：XXX有限公司", 14)
            + TableMaker.td_spin(date_str, 12)
            + TableMaker.td_spin("单位：元", 8)
        )
        line2 = TableMaker.tr(
            TableMaker.td_spin("", 5)
            + TableMaker.td_spin("工资部分", 5)
            + TableMaker.td_spin("出勤", 4)
            + TableMaker.td_spin("应扣项目", 4)
            + TableMaker.td_spin("应发", 5)
            + TableMaker.td_spin("公司部分", 3)
            + TableMaker.td_spin("代缴项目", 4)
            + TableMaker.td_spin("", 4)
        )
        line3 = ""
        for item in line3data:
            line3 += TableMaker.td(item)
        line3 = TableMaker.tr(line3)

        return line0 + line1 + line2 + line3

    @staticmethod
    def pack_up(name, salary_title, manager, date_str, personal_part):  # 表格总输出,根据输入返回完整的表格+前后段落
        content = ''
        personal_line = ''
        table = ''
        opening = [
            "   " + name + "您好：",
            "感谢你对公司作出的贡献和努力！\n现向您发送" + salary_title + "，公司已代缴个人五险一金、个人所得税！您的工资条明细如下："
        ]
        ending = [
            "如有任何问题或疑问请在3个工作日内与"+manager+"联系，如无则默认为当月工资发放无误。谢谢！",
            "继续加油！"
        ]
        for _open in opening:
            content += TableMaker.p(_open)

        table += TableMaker.table_head_str(date_str, salary_title)
        for element in personal_part:
            personal_line += TableMaker.td(element)
        table += TableMaker.tr(personal_line)
        content += TableMaker.table(table)

        for _end in ending:
            content += TableMaker.p(_end)
        return content


if __name__ == "__main__":
    print(TableMaker.table("TABLE"))
    print(TableMaker.tr("TR"))
    print(TableMaker.td_spin("TD_SPIN", 3))
    print(TableMaker.td("TD"))
    print(TableMaker.p("P"))
    print(TableMaker.salary_str(["TEST1", "TEST2", "TEST3"]))
    print(TableMaker.table_head_str("DATE", "TITLE"))
    test_info = []
    for i in range(34):
        test_info.append(str(i))
    print(TableMaker.pack_up("NAME", "TITLE", "MANAGER", "DATE", test_info))
