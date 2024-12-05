#json.dump()存储一组数
#json.dump()接受两个实参：要存储的数据，以及可用于存储数据的文件对象
import json
numbers= [2,3,4,16,2,17]
filename = "numbers.json"
with open(filename,'w') as f:  # 以写入模式打开这个文件，让json能够将数据写入其中
    json.dump(numbers,f)

#使用json.load()将列表读取到内存中
import json
filename = "numbers.json"
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

print("----------------------------------------------------")

# 如果以前在文件中有存储数据，就加载它。
# 否则，提示用户输入用户名并存储。
import json
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("what is your name?:")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"Welcome, {username}!, you are new")
else:
    print(f"Welcome back {username}")

print("----------------------------------------------------")

# 用函数重构remember_me.py
import json
#如果存储了用户名，就获取它。
def get_sorted_username():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

# 如果没有数据，提示用户输入用户名
def get_new_username():
    username = input("what is your name?:")
#  Need to add
    filename = "username.json"
    with open(filename, 'w') as f:
         json.dump(username, f)
# return and with 要对其
    return username

# 问候用户，并指出其名字
def greet_user():
    username = get_sorted_username()
    if username:
        print(f"Welcome back {username}")
    else:
        username = get_new_username()
        print(f"Welcome, {username}!, you are new")

# call function
greet_user()


