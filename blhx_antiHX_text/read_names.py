#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: read_names.py
@time: 12/14/2018 3:37 PM
"""


def read_names_pinyin(names = "names.csv"):
    f = open(names,"r",encoding = "utf-8")
    result = dict()
    for line in f.readlines():
        hx,pinyin,name = line.split(",")
        result[hx] = pinyin[0]+"("+pinyin[1:]+")"
    return result


def read_names_real_name(names = "names.csv"):
    f = open(names,"r",encoding = "utf-8")
    result = dict()
    for line in f.readlines():
        hx,pinyin,name = line.split(",")
        result[hx] = name.strip("\n")
    return result


if __name__ == "__main__":
    print(read_names_pinyin())
    print(read_names_real_name())
