# 7.3 用用户输入来填充字典 dict
# responses = {}
# # 设置一个标志，指出调查是否继续
# polling_active = True
#
# while polling_active:
#     name = input("what is your name?")
#     response = input("which country do you like?")
#  # 将用户回答填入字典
#     responses[name] = response
# # 看看是否还有人参加调查
#     repeat = input("would you like to let another person respond? (yes/no)")
#     if repeat == 'no':
#        polling_active = False
#     elif repeat !='yes':
#         print("Please choose yes or no")
# 以上主要输入的不是No, 就一直循环
#
# #调查结束，显示结果
# print("\n---Polling results---")
# print(str(len(responses)) + " People attended the polling")
# for name, response in responses.items():
#     print(f"{name} would like to go to {response}")

# #在列表之间移动元素
# unconfirmed_users=["kai","Julie","tim"]
# confirmed_users=[]
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user : {current_user}")
#     confirmed_users.append(current_user)
#
# print("The following users have been verified:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user)
# print(f"Now, {confirmed_users} list is formed")


#define function to do the above:
def change_unconfirmed_to_confirmed_user(un_users,con_users): #并不用指名形参是什么类型
    while un_users:
        current_user = un_users.pop()
        print(f"Verifying user : {current_user.title()}")
        con_users.append(current_user.title())

    #print("The following users have been verified:")

def show_confirmed_user(con_users):
    print("The following users have been verified:")
    for con_user in con_users:
        print(con_user)
    print(f"Now, {con_users} list is formed")


unconfirmed_users = ["Kai","Tim","julie"]
confirmed_users = []

#[:] means keep the original list and only operate copy
change_unconfirmed_to_confirmed_user(unconfirmed_users[:] ,confirmed_users)
show_confirmed_user(confirmed_users)

# print(unconfirmed_users)
# print(confirmed_users)


#传递任意数量的实参
def make_pizza(*toppings):
    name = input("Please enter your name:")
    print(f"Making a pizza for {name.title()} with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('oliver','onion')
make_pizza('Lemon')

print("---------------------------------------------------------------------------------")

# 传递更多参数和任意参数
# more parameters but *toppings should be at the end
def make_pizza(name, size, *toppings):
    print(f"Making a {size} pizza for {name.title()} with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("kai",12,"onion","Orange")
make_pizza("Julie",10,"Juice")
print("---------------------------------------------------------------------------------")

#形参**user_info中的两个星号让Python创建一个名为user_info的空字典,并将收到的所有名称值对都放到这个字典中。
def build_profile (first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] =last
    return user_info

user_profile = build_profile("kai","Yao",location = "Brisbane",suburb = "Thornlands")
print(user_profile)
