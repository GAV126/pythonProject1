# 继承类练习：人力系统
# 员工分为两类：全职员工，兼职员工
# 全职和兼职员工都有姓名，工号属性
# 都具备打印信息（姓名Name，工号id）方法
# 全职有月薪属性 monthly_salary
# 兼职有日薪属性daily_salary，每天工作天数的属性 work_days
# 全职和简直都有计算月薪的方法，但是计算过程不一样calculate_monthly_pay

#father class
class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    def print_info(self):
        print(f"Employee name : {self.name}, Id : {self.employee_id}")

#child class 1
class FullTimeEmployee(Employee):
    def __init__(self,name,employee_id,monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary
    def calculate_monthly_pay(self):
        return self.name +  "'s Monthly Salary is: " + self.monthly_salary
    # use print return None
    # print(self.monthly_salary)

#child class 2
class PartTimeEmployee(Employee):
    def __init__(self,name,employee_id, daily_salary, work_days):
        super().__init__(name,employee_id)
        self.daily_salary = daily_salary
        self.work_days = work_days

# if you do not use int, get error: can't multiply sequence by non-int of type
    def calculate_monthly_pay(self):
        return int(self.daily_salary) * int(self.work_days)

zhangsan = FullTimeEmployee("Tim","PT001","2000")
lisi = PartTimeEmployee("Lisa","PT004","150","15")

zhangsan.print_info()
lisi.print_info()

print(zhangsan.calculate_monthly_pay())
print(lisi.calculate_monthly_pay())


