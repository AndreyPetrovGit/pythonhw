def char_freq(string):
    dic = {}
    for i in string:
        s = i + ""
        if(s in dic):
            dic[s] = 0
        else:
            dic[s] = dic[s] + 1
    return dic
print(char_freq("aaabbc"))
