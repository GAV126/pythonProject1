# 访问字典里的值
alien_0 ={"colour":"green","points":5}
print(alien_0["colour"])
# 添加键值对
alien_0["X_P"]=0
alien_0["Y_P"]=10
print(alien_0)
# 修改字典的值
alien_0["X_P"]=20
print(alien_0)

alien_0 = {"X":0,"Y":10,"speed" : "fast"}
if alien_0["speed"]=="slow":
    x_increment = 1
elif alien_0["speed"]=="fast":
    x_increment = 2
alien_0["X"] = alien_0["X"] + x_increment
print(f"new position is {alien_0["X"]}")

#6.2.7
# get()在指定的键不存在时返回一个默认值
zimu = {"a":"A","b":"B","c":"C"}
x = zimu.get("a","not exist")
print(x)

user = {"name":"kai", "age":18, "sex":"male"}
name = user["name"]
age = user["age"]
print(name)
print(f"your name is {name}, and you age is {age}")
print("-------------------------------------------------------------------------")

# 遍历一个字典
lang = {"kai":"Spanish","Julie":"Chinese","Tim":"Malay"}
for name, language in lang.items():   # two variables represent key and value
    print(f"{name}'s like is {language}")

# 遍历所有的值，用set去获取唯一值
lang = {"kai":"Spanish","Julie":"Chinese","Tim":"Malay","Andy":"Malay"}
for value in set(lang.values()):  #items, keys, values
    print(f"{value}")

print("--------------------------------------------------------")

lang = {"kai":"Spanish","Julie":"Chinese","Tim":"Malay"}

friend = ["Tim","Ada","kai"]
for name in lang.keys():
    print(f"hi,{name}")

    if name in friend:
        language = lang[name]
        print(f"{name}, i see you love {language}")

print("-----------------------------------------------------")

lang = {"kai":"Spanish","Julie":"Chinese","Tim":"Malay"}

if 'erin' not in lang.keys():
    print("erin, please go there")

print("-----------------------------------------------------")

working_years={"kris":5,"kai":1.5, "yvette":4}

for name, year in working_years.items():
    print(f"{name}, you have been working in council for {year} years")

print("-----------------------------------------------------")

# 排序
working_years={"kris":5,"kai":1.5, "Andy":1,"yvette":2}
for name  in sorted(working_years.keys()):
    print(f"{name}, you have been working in council for X years")

print("Next is 6.4.1-----------------------------------------------------")

# 打印多个字典 - 首先创建三个字典，其中每个字典都表示一个外星人。然后将这些字典都存储到一个名为aliens的列表中
alien_0 = {"colour":"green","speed":"slow"}
alien_1 = {"colour":"red","speed":"fast"}
alien_2 = {"colour":"blue","speed":"slow"}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

print("Next is 6.4.1-----------------------------------------------------")

# 6.4.1
aliens=[]   # 首先创建一个空列表，用于存储接下来将创建的所有外星人
for alien_number in range(30):
    new_alien = {"colour":"green","points":5,"speed":"slow"}
    aliens.append(new_alien)
for alien in aliens[:5]:
# 打印列表里的值
    print(alien)
print("......")
# 打印列表
print(aliens)
print(f"total number of aliens are {len(aliens)}")
print("-----------------------------------------------------")

aliens=[]
for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien["colour"]=="green":
        alien["colour"]="red"
        alien["points"] = 9
        alien["speed"] = "fast"
for alien in aliens[:5]:
    print(alien)
print("Next is 修改 value in for -----------------------------------------------------")

# 修改value
aliens=[]
for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien["colour"]=="green":
         alien["colour"]="red"
         alien["points"] = 9
         alien["speed"] = "fast"
    elif alien["colour"]=="red":
         alien["points"] =100
for alien in aliens[:5]:
    print(alien)
print("-----------------------------------------------------")

#　在字典中存储列表
pizza = {"crust":"thick","toppings":["meat","cheese"]}

print(f"you've order a {pizza["crust"]} pizza with the following toppings:")
for topping in pizza["toppings"]:
    print("\f" + topping)

print("-----------------------------------------------------")
# interesting result
# lang = {"kai":["Spanish","Korean"],"Julie":"Chinese","Tim":"Malay"}
# 如果是列表["Spanish"]这个长度是1，如果不是列表,长度是7

#6.4.2　在字典中存储列表
# Need two for
# New practice 6.4.2
# 为进一步改进这个程序，可在遍历字典的for循环开头添加一条if语句，
# 通过查看len(languages)的值来确定当前的被调查者喜欢的语言是否有# 多种。如果他喜欢的语言有多种，就像以前一样显示输出；如果只有一种，
# 就相应修改输出的措辞，如显示Sarah's favorite language is # C。

lang = {"kai":["Spanish","Korean"],"Julie":["Chinese","Polish"],"Tim":["Malay"]}

for name , languages in lang.items():
    if len(languages)>1:
       print(f"\n{name}'s language are:")
       for language in languages:
         print(f"{language.title()}")
    else:
        print(f"\n{name}'s language is:")
        for language in languages:
          print(f"{language.title()}")


