for letter in 'freeCodeCamp':
    if letter == "e":
        break
    print('letter :', letter)
print("is that right?")

for num in range (2,10):
    if num%2==0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")

for num in range (2,10):
    if num%2==1:
        print(f"{num} is a even number")
        break
    print(f"{num} is a odd number")
print("level with for")

current_number = 0
while current_number <10:
    current_number+=1
    if current_number %2 ==0:
        continue
    print(current_number)

i = 0
while i<5:
    print(i)
 # without the following, it will run infinitely
    i+=1