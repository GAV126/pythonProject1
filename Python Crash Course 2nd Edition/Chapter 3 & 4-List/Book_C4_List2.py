students= ["kai","julie","Tim"]
for student in students:
    print(f"Hey, {student.title()}")

# 使用函数range
for value in range(1,5):
    print(value)

# 创建数字列表
numbers = list(range(1,11,2))
print(numbers)

#创建列表例子
squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)

#切片
players = ["kai","tim","andy","Kris","Yvette"]
print(players[1:3])
print(players[:3])

# 遍历切片
players = ["kai","tim","andy","Kris","Yvette"]
length = len(players)
print(f"Here are {length} players in our team")
for player in players[:5]:  #遍历前5名队员
    print(player.title())
# 注意差异
for player in players[4]:   #遍历第5名队员名字
    print(player.title())

# copy a list
players = ["kai","tim","andy","Kris","Yvette"]
amatuer_players = players[:]   # 要复制列表，可创建一个包含整个列表的切片
print(players)
print(amatuer_players)

#元组
# 不可以修改元组元素
# dimension = (200,50)
# dimension[0]=111

#但可以给元组重新赋值
dimension = (200,50)
print("Original dimestion :")
for di in dimension:
    print(di)

dimension = (210,51)
print("Original dimestion :")
for di in dimension:
    print(di)
