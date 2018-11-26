# OneEmailInfo.py

> Shawn
> 11/26/2018


这个类用于传递ReadXLSX获取的数据.

专门编写一个类可以将数据打包得更人性化.

虽然可以直接用一个数组来传递,但是谁又愿意专门写一个文档去标注索引和信息的对应关系呢?

软件本体见 https://blog.csdn.net/weixin_41084236/article/details/84325652

----

```python
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
```

这是个简单的用于数据传递的类. 构造方法和toString方法都是依照个人喜好完成的.

toString方法能够快速打印出类的内容, 方便测试使用.