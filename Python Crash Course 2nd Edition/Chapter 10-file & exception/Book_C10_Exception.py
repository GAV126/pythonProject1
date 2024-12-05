# print("Give me two numbers, and i will divide them for you")
# print("Enter q to quit.")
#
# while True:
#     first_number = input("First number:")
#     if first_number == 'q':
#        break
#     second_number = input("Second number:")
#     if first_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Error")
#     else:
#         print(answer)
#     break
#
# print("-----------------------------------------------------------------")
#
# # How to make sure the user enters a number (integer)
# def inputNumber(message):
#     while True:
#         try:
#             userInput = int(input(message))
#         except ValueError:
#             print("Not an integer! Try again.")
#             continue
#         else:
#             return userInput
#             break
#
#         # MAIN PROGRAM STARTS HERE:
#
# age = inputNumber("How old are you?")
#
# if (age >= 18):
#     print("You are old enough to vote.")
# else:
#     print("You will be able to vote in " + str(18 - age) + " year(s).")
#
# print("-----------------------------------------------------------------")
from For import count


# filename = "data.txt"
# try:
#     with open(filename, encoding="utf-8") as f:
#         contents = f.read()
# except FileNotFoundError:
#     print("Not found")
# else:
# # 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中
#     words = contents.split()
#     print(words)
#     num_words = len(words)
#     print(f"The file {filename} has about {num_words} words.")
#
# print("-----------------------------------------------------------------")

# Create a function
def count_words(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
         print(f"{filename} Not found")
 # use pass will do nothing. user does not know the error
         # pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ["noexist.txt","poem.txt","data.txt","12313.py"]
for a in filenames:
    count_words(a)
print("-----------------------------------------------------------------")

while True:
      try:
         b=int(input("please enter a number:"))
      except ValueError:
           print("not a number:")
           continue
      else:
           print(b)
           break