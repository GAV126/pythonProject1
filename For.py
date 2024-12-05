# # only list
# temp_list = [36,36,37,37,38,39,40]
# for a in temp_list:
#     if a>=38:
#         print(a)
#         print("Out!")
#---------------------------------------------------------------------------
# use dictionary
#
# temp_dict= {"111":36.4,"112":36.6,"113":37.1,"114":38.9,"115":40.1}
# for staff_id, temp in temp_dict.items():
#     if temp >=38:
#         print(staff_id + "\'s temperature is:" + str(temp))
# ---------------------------------------------------------------------

# # use range
# for num in range(1,10,1):
#     print(num)
#
# #---------------------------
# total = 0
# for i in range (1,101):
#     total = total +i
# print(total)

# # while
# list = ["D","V","L","\\'"]
# i=0
# while i<len(list):
#     print(list[i])
#  # if there is no i=i+1, it will come to forever ture and run
#     i=i+1
# print('------------------------------------------------------')
#
# for i in list:
#     print(i)
# print('------------------------------------------------------')
#
# for i in range(len(list)):
#     print(list[i])
# print('------------------------------------------------------')

#practice
print("Hello, i can help you calculate avg")
total = 0
count=0
user_input=input("Please enter you number and when you finish, please hit q:")
while user_input !="q":
    num=float(user_input)
    total = total + num
    count= count+1
    user_input = input("Please enter you number and when you finish, please hit q:")
if  count==0:
    result=0
else:
    result = total / count
print ('Avg = ' + str(result))
print('------------------------------------------------------')

