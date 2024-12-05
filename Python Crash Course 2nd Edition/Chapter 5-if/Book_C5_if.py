cars = ["bmw","toyota","byd"]
for car in cars:
    if car =="bmw":
        print(car.upper())
    else:
        print(car.title())
# 检查特定值是否包含在列表中
if "Kia" in cars:
    print("y")
else:
    print("N")

# if else and elif
# if-elif-else 不一定要有else，而且一个测试通过后，就会跳过余下的
cars = ["bmw","toyota","byd"]
if "bmw" in cars:
    print(f"my car is {cars[0].title()}")
elif "kia" in cars:
    print(f"This is Kia")
elif "byd" in cars:
    print(f"This is byd")

# 确定列表不空
cars=[]
if cars:
    for car in cars:
        print(f"this is {car}")
    print(f"this is all cars")
else:
    print(f"nothing in the list")

