# . 表示当前文件夹
# 待读文件和代码文件是在同一个文件夹下

# use read()
f=open("../data.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

# use with form, do not need to close()
print("-------------------")
with open("../data.txt", "r", encoding="utf-8") as f:
    content =f.read()
    print(content)

#use readline
print("-----------------------")
# readline 会把每行的换行符读出来， 同时print 本身自身自带换行符。两个换行就多出来一个空行。
with open("../data.txt", "r", encoding="utf-8") as f:
     print(f.readline())
     print(f.readline())

#use readlines
print("-----------------------")
with open("../data.txt", "r", encoding="utf-8") as f:
    print(f.readlines())

print("-----------------------")
with open("../data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)