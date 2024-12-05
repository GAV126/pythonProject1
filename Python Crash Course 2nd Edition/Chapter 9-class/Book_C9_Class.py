#from pydoc import describe


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is rolling over")

my_dog = Dog("Peanut",2)
print(f"my dog's name is {my_dog.name}")
print(f"my dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()

print("-----------------------------------------------------------")

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
 # need to use print to show the value if the function uses 'return'
        return long_name.title()
    def read_odometer(self):
        print(f"This can has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
           self.odometer_reading = mileage
        else:
            print(f"As {mileage} is less than {self.odometer_reading}, You cannot roll back the odometer")
    def increment_odometer(self,miles):
        if miles >=0:
           self.odometer_reading += miles
        else:
            print("Please enter a positive number")

my_car = Car('Toyota',"RAV4",2024)

print(my_car.get_descriptive_name())

# Directly change value
my_car.odometer_reading = 100
my_car.read_odometer()

my_car.update_odometer(300)
my_car.read_odometer()

my_car.increment_odometer(101)
my_car.read_odometer()

# 创建电动汽车子类
class ElectricCar(Car):
    def __init__(self, make, model, year) :
# 初始化父类属性
        super().__init__(make, model, year)
# 在初始化电动汽车自己的属性
        self.battery_size =75
    def describe_battery(self):
        print(f"This {self.make} {self.model} has a {self.battery_size}-kWh battery")
my_tesla = ElectricCar("Tesla","Model Y","2025")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

print("------------------------------------------------------------------------------")

#此处的代码将battery单独独立出来。这是唯一与上边代码不同的地方。

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This can has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
           self.odometer_reading = mileage
        else:
            print(f"As {mileage} is less than {self.odometer_reading}, You cannot roll back the odometer")
    def increment_odometer(self,miles):
        if miles >=0:
           self.odometer_reading += miles
        else:
            print("Please enter a positive number")

my_car = Car('Toyota',"RAV4",2024)

print(my_car.get_descriptive_name())

#创建电池类
class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")
    def get_range(self):
        if self.battery_size ==75:
            range = 260
        elif self.battery_size ==100:
            range = 315
        else:
            range = 500
        print(f"This car cao go about {range} miles on a full charge")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
#添加属性self.battery。 我个人认为这就是这个类和Battery类关联的地方
#添加了一个名为self.battery的属性,这行代码让Python创建一个新的Battery实例（因为没有指定容量，所以为默认值75），并将该实例赋给属性self.battery。
#这行代码让Python在实例my_tesla中查找属性battery，并对存储在该属性中的Battery实例调用方法describe_battery()。
        self.battery = Battery()

my_byd = ElectricCar("BYD","Seal","2024")
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()

