bicycles = ["trek","redline","99bike"]
print(bicycles[1].title())

# change content
bicycles[1] = "Giant"
print(bicycles[1].title())

# 添加元素在末尾
bicycles.append("Steal")
print(bicycles)

# 指定位置插入数值
bicycles.insert(1,"ABC")
print(bicycles)

# 用pop，弹出最后一个值
popped_bicycle = bicycles.pop()
print(f"the last value is : {popped_bicycle}")
print(bicycles)

# 用pop指定弹出哪个值
first_bike = bicycles.pop(0)
print(f"my first bike is {first_bike.title()}")

# sort方法永久改变顺序; sorted 是临时改变
print(bicycles)
bicycles.sort(reverse=True)
print(f"after sort is {bicycles}")

#reverse()不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
bicycles.reverse()
print(f"after reverse : {bicycles}")

# length
print(len(bicycles))