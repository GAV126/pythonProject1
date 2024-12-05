#7.4
# while True:
#      ingredient = input("Please enter what ingredient you need (if you want to quit,please enter 'quit'):")
#      if ingredient=='quit':
#          break
#      else:
#       print(f"Yes, we will add {ingredient} to your Pizza")
# print("-------------------7.5 will start---------------------------------------------------------------")

#7.5
# while True:
#      age = input("Please enter your age:")
#      if age == 'quit':
#          break
#      elif int(age)<3:
#          print("You are free to admit")
#      elif 3 <= int(age) <= 12:
#          print("You need to pay $10")
#      else:
#          print("You need to pay $15")
#
# print("-------------------7.8 will start---------------------------------------------------------------")

#7.8 在列表之间移动元素
# sandwich_orders = ["seafood","Pizza melt","Italian","seafood","seafood"]
# finished_sandwiches=[]
# while sandwich_orders:
#     current_order = sandwich_orders.pop()
#     print(f"I am working on your {current_order} sandwich")
#     finished_sandwiches.append(current_order)
# print(finished_sandwiches)
# for finish in finished_sandwiches:
#     print(f"{finish} sandwich is finished")

print("-------------------------7.9 will start---------------------------------------------------------------")

#7.9 删除为特定值的所有列表元素
sandwich_orders = ["seafood","Pizza melt","Italian","seafood","seafood"]
finished_sandwiches=[]
print("We are out of seafood today")
while "seafood" in sandwich_orders:
    sandwich_orders.remove("seafood")
print("\n")
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I am working on your {current_order} sandwich")
    finished_sandwiches.append(current_order)
print(finished_sandwiches)
for finish in finished_sandwiches:
    print(f"{finish} sandwich is finished")

print("-------------------------7.10 will start---------------------------------------------------------------")
#使用用户输入来填充字典
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
