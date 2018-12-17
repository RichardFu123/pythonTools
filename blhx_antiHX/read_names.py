def read_names_pinyin(names = "names.csv"):
    f = open(names,"r",encoding = "utf-8")
    result = dict()
    for line in f.readlines():
        hx,pinyin,name = line.split(",")
        result[hx] = pinyin[1:]
    return result



def read_names_real_name(names = "names.csv"):
    f = open(names,"r",encoding = "utf-8")
    result = dict()
    for line in f.readlines():
        hx,pinyin,name = line.split(",")
        result[hx] = name[:-1]
    return result




if __name__ == "__main__":
    print(read_names_pinyin())
    print(read_names_real_name())
