#5-7
favorite_fruits = ['blueberries', 'apples', 'peaches']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")

print("---------------------5.8,5.9 Option 1 will start---------------------------------------------")

#5-8 & 5.9
users = ["admin","kai","Julie","Tim","Jim"]
if len(users)== 0:
    print("We need to find some users!")
else:
     for user in users:
        if user == "admin":
           print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")


print("---------------------5.8,5.9 Option 2 will start---------------------------------------------")
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for login in again!")
else:
    print("We need to find some users!")


print("---------------------5.10 will start--------------------------------------------------------")

# 5.10
current_users= ["admin","kai","Julie","Tim","Jim"]
current_users_lower = [user.lower() for user in current_users]  # 把list里的全部小写
print(current_users_lower)
new_users =  ["Andy","kai","julie","Kris","Kerry"]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"User '{new_user}' exists, please user a new name")
    else:
        print(f"you can use '{new_user}'")

print("---------------------5.11 will start--------------------------------------------------------")
# 5.10
numbers = list(range(1,10))  # 生成list
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")