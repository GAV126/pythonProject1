filenames = ["cats.txt", "dogs.txt"]
for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
       with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
          print(f"Sorry, I can't find {filename}.")

print("--------------------------------------------------")
print("----")
pets=[]
pet = {"name":"huahua","owner":"kai"}
pets.append(pet)
pet = {"name":"wangcai","owner":"Julie"}
pets.append(pet)
pet = {"name":"huahua","owner":"kai"}
pets.append(pet)
pet = {"name":"miaomiao","owner":"Gavin"}
pets.append(pet)
print(pets)
for pet in pets:
    name = pet["name"]
    owner = pet["owner"]
    print(f"{name}'s owner is {owner}")  #print should be in1111