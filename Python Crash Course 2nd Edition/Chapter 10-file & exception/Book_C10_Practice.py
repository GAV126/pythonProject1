# #10-1
# print("#读取这个文件")
# filename="learning_python.txt"
# with open(filename) as file_object:
#     content = file_object.read()
# print(content)
#
# print("#遍历文件对象")
# filename="learning_python.txt"
# with open(filename) as file_object:
#      for line in file_object:
#          print(line.rstrip())
#
# print("各行存储在一个列表中")
# filename="learning_python.txt"
# with open(filename) as file_object:
#      lines=file_object.readlines()
# print(lines)
# for line in lines:
#          print(line.rstrip())
#
# print("Python都替换为另一门语言的名称")
# filename="learning_python.txt"
# with open(filename) as file_object:
#      lines=file_object.readlines()
# print(lines)
# for line in lines:
#          print(line.replace("Python","C").strip())
#
#
# #10-3 编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中。
# name = input("Enter your name:")
# filename = "guest.txt"
# with open(filename,"w") as f:
#     f.write(name)
# print("-----------------------------10.4 will start-------------------------")
#
#
# #10-4 编写一个while循环，提示用户输入名字。用户输入名字后，在屏幕上打印一句问候语，并将一条到访记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
# filename = "guest_book.txt"
# while True:
#     name = input("Enter your name:")
#     if name == 'quit':
#         break
#     else:
#        with open(filename, "a") as f:
#           f.write(f"{name}\n")
#        print(f"Welcome, {name}, you have been added!")
#
# #10-5 用户输入，存入List，再写入文件
#
# # 错误：with 应该写在最外边，否则最后一个输入无法写入文件。
# filename = 'programming_poll.txt'
# responses = []
# while True:
#     response = input("Why you love Python:")
#     responses.append(response)
#
#     continue_pool= input("Would you like to let someone else respond? (y/n) ")
#     if continue_pool != 'y':
#         break
#     else:
#        with open(filename, "a") as f:
#           for response in responses:
#               f.write(f"{response}\n")
# print(responses)
# print("----------------------------The following is correct--------------------------------")
#
# # 正确：
# filename = 'programming_poll.txt'
# responses = []
# while True:
#     response = input("Why you love Python:")
#     responses.append(response)
#
#     continue_pool= input("Would you like to let someone else respond? (y/n) ")
#     if continue_pool != 'y':
#         break
# # 注意with要写在最外边
# with open(filename, "a") as f:
#     for response in responses:
#        f.write(f"{response}\n")
# print(responses)
# print("-------------------------10-6 will start---------------------------------------")

#10-6
# try:
#     num1 = int(input("Please enter the first number:"))
#     num2 = int(input("Please enter the second number:"))
# except ValueError:
#     print("Please enter a number")
#
# else:
#     sum = num1+num2
# print(sum)
#
# print("-------------------------10-7 will start---------------------------------------")
# flag = True
# while flag:
#     try:
#         num1 = int(input("Please enter the first number:"))
#         num2 = int(input("Please enter the second number:"))
#     except ValueError:
#         print("Please enter a number")
#         continue
#     else:
#         sum = num1 + num2
#         flag = False
#     print(sum)
#
# print("-------------------------10-8 will start---------------------------------------")

# #10.8 两个文件，读出里边内容
# filenames = ["cats.txt", "dogs.txt"]
# for filename in filenames:
#     print(f"\nReading file: {filename}")
#     try:
#        with open(filename) as f:
#             content = f.read()
#             print(content)
#     except FileNotFoundError:
#           print(f"Sorry, I can't find {filename}.")
#
# print("-------------------------10-10 will start---------------------------------------")
# filename = "PlaySession.txt"
# try:
#      with open(filename,encoding='utf-8') as f:
#           content = f.read()
#  #         print(content)
# except FileNotFoundError:
#     print(f"{filename} does not exist")
# else:
#  #   num = content.lower().count("the")
#      word = "the "
#      num = content.count(word)
#      print(f"'{word}' appears in {filename} about {num} times.")
#
# print("-------------------------The following use function---------------------------------------")
#
# # use function
# def count_common_words(filename, word):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             content = f.read()
#     #         print(content)
#     except FileNotFoundError:
#         print(f"{filename} does not exist")
#     else:
#         #   num = content.lower().count("the")
#         num = content.count(word)
#         print(f"'{word}' appears in {filename} about {num} times.")
#
# count_common_words("PlaySession.txt","the ")
# print("-----------------------------------------------10-11 will start--------------------")

#10-11
import json
while True:
 try:
   like_num = int(input("please enter your number:"))
   filename = "best.json"   # need ""
   with open(filename,"w") as f:
     json.dump(like_num,f)
     print("Thanks! I'll remember that.")
     break
 except ValueError:
     print("Please enter a number")
     continue

# 打开原有文件
with open(filename) as v:
    content = v.read()
print(f"{content} is the value from the read()")

#打开json文件
import json
filename = "best.json"
with open(filename) as f:
    content = json.load(f)
print(f"{content} is the value from Json file")
print(f"I know your favorite number! It's {content}")

print("-----------------------------------------------10-12 will start--------------------------")

#10-12 将上一个联系中的两个部分合二为一
import json
filename = "best1.json"
try:
   with open(filename) as f:
       content = json.load(f)
except FileNotFoundError:
    like_num = int(input("please enter your number:"))
    with open(filename,"w") as v:
        json.dump(like_num,v)
    print(f"Now,{like_num} is added to {filename}")
else:
    print(f"I know your favorite number! It's {content}")

print("-----------------------------------------------10-13 will start----------------------------")

#10-13 只更新greet_user()。整个程序参见"用函数重构remember_me.py"
def greet_user():
    username = get_sorted_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"Welcome, {username}!, you are new")











