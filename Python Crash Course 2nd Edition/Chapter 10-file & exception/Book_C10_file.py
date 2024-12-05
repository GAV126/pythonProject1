# 读取整个文件
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents.rstrip())

print("--------------------------------------------------------")

# 逐行读取文件
filename = "pi_digits.txt"
# open 返回的文件对象只能在with代码块内部使用
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("--------------------------------------------------------")

#在with代码块中将文件的各行存在一个列表中,这样可以在with外用文件内容
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()  # 方法readlines()从文件中读取每一行，并将其存储在一个列表中
print(lines)
for line in lines:
    print(line.rstrip())

print("--------------------------------------------------------")

# 使用文件内容,拼接
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines() # 打开文件，并将其中所有的行都存储在一个列表中
pi_string = ''
for line in lines:
    pi_string = pi_string + line.strip()
# 下只打印小数点后10位
print(pi_string[:20])
print(len(pi_string))

print("--------------------------------------------------------")

# checking if certain number is in Pi
# filename = "pi_digits.txt"
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string = pi_string + line.strip()
# birthday = input("Enter your birthday in mmddyy:")
# if birthday in pi_string:
#     print("Yes")
# else:
#     print("No")

# write to file
# 以写入模式
# （'w'）打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件的内容
filename = "Programming.txt"
with open(filename,"w") as f:
    f.write("I love Python.\n")
    f.write("I love Python1.\n")

filename = "Programming.txt"
with open(filename,"a") as f:
    f.write("I love Python2.\n")
    f.write("I love Python3.")


# 分析文本
filename = "alice.txt"

try:
    with open(filename,encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    #计算该文件包含多少单词
    words = content.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

#用函数实现
print("以下用函数实现")
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
         print(f"Sorry, the file {filename} does not exist.")
       # pass # pass什么都不做
    else:
        # 计算该文件包含多少单词
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filename = "guest_book.txt"
count_words(filename)

#以下查询多个文件,注意函数的调用方式
print("以下查询多个文件")
filenames=['alice.txt','guest_book.txt','12.txt']
for filename in filenames:
    count_words(filename) # 在for循环中调用函数
