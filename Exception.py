# #1
# while True:
#     try:
#        age = int(input("Please enter your age: "))
#     except ValueError:
#         print("Sorry, I didn't understand that.")
#         #better try again... Return to the start of the loop
#         continue
#     else:
#         #age was successfully parsed!
#         #we're ready to exit the loop.
#         break
# if age >= 18:
#     print("You are able to vote in the United States!")
# else:
#     print("You are not able to vote in the United States.")
#
# print("--------------------------------------------------------------------------")
#
# while True:
#     try:
#         age = int(input("Please enter your age: "))
#         if age >= 18:
#             print("You are able to vote in the United States!")
#         else:
#             print("You are not able to vote in the United States.")
#     except Exception as e:
#         print("please enter number")
#
# #2 only Capital is valid
# while True:
#     data = input("Please enter a loud message (must be all caps): ")
#     if not data.isupper():
#         print("Sorry, your response was not loud enough.")
#         continue
#     else:
#         #we're happy with the value given.
#         #we're ready to exit the loop.
#         break
#
# # only A,B,C,D are valid value
# while True:
#     data = input("Pick an answer from A to D:")
#     if data.lower() not in ('a', 'b', 'c', 'd'):
#         print("Not an appropriate choice.")
#     else:
#         break
#
# #3 use function
# def get_non_negative_int(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#         except ValueError:
#             print("Sorry, I didn't understand that.")
#             continue
#
#         if value < 0:
#             print("Sorry, your response must not be negative.")
#             continue
#         else:
#             break
#     return value
#
# age = get_non_negative_int("Please enter your age: ")
# kids = get_non_negative_int("Please enter the number of children you have: ")
# salary = get_non_negative_int("Please enter your yearly earnings, in dollars: ")
#
# 4
# import math
# while True:
#   try:
#     x = int(input('Please enter a positive number:\n'))
#     try:
#         print(f'Square Root of {x} is {math.sqrt(x)}')
#         break
#     except ValueError as ve:
#         print(f'You entered {x}, which is not a positive number.')
#         continue
#   except ValueError as ve:
#     print('You are supposed to enter positive number.')
#     continue
#
# 5 check ip
# while True:
#     try:
#         HOST = input('Enter host IP: ')
#         if len(HOST.split(".")) != 4:
#             raise ValueError
#         for char in HOST:
#             if char not in "0123456789.":
#                 raise ValueError
#     except ValueError:
#         print('Error. 111That is not a valid IP address.')
#         continue
#     else:
#         break
#
flag = True
while flag:
    try:
        num1 = int(input("Please enter the first number:"))
    except ValueError:
        print("Please enter the first number")
        continue
    while True:
      try:
        num2 = int(input("Please enter the second number:"))
        sum = num1 + num2
        flag = False
        print(sum)
        break
      except ValueError:
        print("Please enter a number")


