# 在一个名字为poem.txt 的文件里，写入一下内容

with open("../poem.txt", "w", encoding ="utf-8") as f:
    f.write("11 \n")
    f.write("22 \n")
    f.write("33 \n")
    f.write("444 \n555\n666")

print("----------------------------------------------------")
# if use write again, it will wipe out the existing content
with open("../poem.txt", "w", encoding ="utf-8") as f:
    f.write("4441 \n5551\n6661\n")

# 在上面的poem.txt文件结尾处，添加以下两句：
with open("../poem.txt", "a", encoding ="utf-8") as f:
    f.write("qqq\n")
    f.write("ppp\n")