# if you enter an non-int value, will get an error
# age = input("how old are u?")
# if age.isdigit():
#    print(f"you are {age} years old ")
#    if int(age) >=18:
#     print(f"{age} means you are adult")
#    else:
#     print(f"{age} means you are not an adult")
# else:
#     print("Invalid input,please enter an int number")
#
# print("------------------------------------------------------------------------")
from operator import truediv

# if there is an invalid value, keep asking until a valid value is entered
# while True:
#     try:
#         # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
#         age = int(input("Please enter your age: "))
#     except ValueError:
#         print("Sorry, I didn't understand that.")
#         #better try again... Return to the start of the loop
#         continue
#     else:
#         #age was successfully parsed!
#         #we're ready to exit the loop.
#         break
# if int(age) >= 18:
#     print(f"{age} means you are adult")
# else:
#     print(f"{age} means you are not an adult")

# print("------------------------------------------------------------------------")
# number = int(input("please enter a number and I will let you it is an odd or even:"))
# if number%2==0:
#     print(f"{number} is an even")
# else:
#     print(f"{number} is an odd")
# print("------------------------------------------------------------------------")

#7.2 while
# current_number = 0
# while (current_number)<=5:
#     print(current_number)
#     current_number+=1

# T0 add up value 0-5
# total = 0
# current_number = 0
# while (current_number)<=5:
#     total = total +current_number
#     current_number+=1
# print(total)

# 7.2.4 set flag
promt = "Please enter sth, and then i will repeat:\n"
promt += "Enter 'quit' will leave here:"
active = True
while active:
    message = input(promt)
    if message =='quit':
        print("we are going to leave")
        active = False
    else:
        print(message)
        continue