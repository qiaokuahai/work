import itertools as its


words_num = "1234567890"
words_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
r = its.product(words_num, repeat=7)
with open("password.txt", "w") as dic:
    d = []
    for i in r:
        d.append("".join(i) + "\n")
    dic.writelines(d)
