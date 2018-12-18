#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: antiHX_text.py
@time: 12/14/2018 3:37 PM
"""
import core


if __name__ == "__main__":
    with open("output.txt","w",encoding = "utf-8") as f:
        tp = input("选择翻译模式:1 原名,2 注音: ")
        hx = input("输入原文: ")
        if tp == "1":
            content = core.anti_HX(hx)
        elif tp == "2":
            content = core.anti_HX(hx,"pinyin")
        else:
            raise Exception("wrong anti_HX type")
        print(content)
        f.write(content)
