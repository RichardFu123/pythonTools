#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: core.py
@time: 12/14/2018 3:37 PM
"""
import read_names


def anti_HX(string,type = "real_name"):
    pinyin = read_names.read_names_pinyin()
    real_name = read_names.read_names_real_name()
    source = real_name
    if type == "pinyin":
        source = pinyin
    result = string[:]
    for hx in source.keys():
        result = result.replace("祥凤","xiangfeng")
        result = result.replace(hx,source[hx])
    result = result.replace("xiangfeng","祥凤")
    return result


if __name__ == "__main__":
    print(anti_HX("本期特定加成角色萨拉托加、猋(鸟海)、貆(川内)、桐(吹雪)、柚(绫波)、狻(三隈)、猨(最上)、鸱(飞鹰)、鸢(隼鹰)、獒(高雄)、犮(摩耶)、狏(那智)、梓(雷)、柏(电)、獌(妙高)、鹞(祥凤)、貎(神通)"))
    print(anti_HX("本期特定加成角色萨拉托加、猋(鸟海)、貆(川内)、桐(吹雪)、柚(绫波)、狻(三隈)、猨(最上)、鸱(飞鹰)、鸢(隼鹰)、獒(高雄)、犮(摩耶)、狏(那智)、梓(雷)、柏(电)、獌(妙高)、鹞(祥凤)、貎(神通)","pinyin"))

