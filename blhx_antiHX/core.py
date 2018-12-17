import read_names

def anti_HX(string,type = "real_name"):
    pinyin = read_names.read_names_pinyin()
    real_name = read_names.read_names_real_name()
    source = real_name
    if type == "pinyin":
        source = pinyin
    result = string[:]
    for hx in source.keys():
        result = result.replace(hx,source[hx])
    return result


if __name__ == "__main__":
    print(anti_HX("苓"))
    print(anti_HX("菡","pinyin"))

