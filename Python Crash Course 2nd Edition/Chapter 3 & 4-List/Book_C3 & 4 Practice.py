#3.4 - 3.7
guest= ["kai","andy","tim","sb"]
name = guest[0].title()
print(f"{name}, please come to dinner")
print(f"{guest[3]} cannot attend, let me remove him.....")
del(guest[3]) # 删除
new_name = "Tina"
guest.append(new_name)
print(guest)
guest.insert(0,"Yvette")
guest.insert(2,"Matt")
print(guest)
print("Sorry, we can only invite two guests, now let me delete......")
# 只留下两位客人
while len(guest)>2:
      current=guest.pop()
      print(f"Sorry, {current}, Please go away")
      del(current)
# check who is still invited
for people in guest:
    print(f"Hi,{people}, please back" )

# delete the rest of two guests
while len(guest)>0:
      current=guest.pop()
      print(f"Sorry, {current}, Please go away")
      del(current)
print(guest)


#4.3
for x in range(1,6):
      print(x)
# 明确是一个list
numbers = list(range(1,4))
for number in numbers:
      print(number)
print(numbers)

#4.5
number =  list(range(1,100001))
print(min(number))
print(max(number))
print(sum(number))

#4.6
numbers = list(range(1,20,2))
for number in numbers:
      print(number)

#4.7
numbers = list(range(3,31))
for number in numbers:
      if number % 3==0:
            print(number)
# option B
threes = list(range(3, 31, 3))

for number in threes:
    print(number)

#4.8 把结果存入list. 注意与前边几个联系的差异
cube_list =[]
for number in range(1,11):
      cube = number **3
      cube_list.append(cube)
      print(cube)
print(cube_list)

#4.11
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]  # 要复制列表，可创建一个包含整个列表的切片
favorite_pizzas.append("Beef")
friend_pizzas.append("Chicken")
for favorite_pizza in favorite_pizzas:
      print(f"My favorite pizzas are:{favorite_pizza}")
for friend_pizza in friend_pizzas:
      print(f"My friend's favorite pizzas are:{friend_pizza}")


#4.13 tuple
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print(f"- {item}")





