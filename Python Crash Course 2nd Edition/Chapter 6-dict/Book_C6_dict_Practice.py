#6.5
rivers={"nile":"Egypt","Yellow":"China","Brisbane river":"Aus"}
for name, country in rivers.items():
    print(f"-The {name} runs through {country}")
print("\n")
for name in rivers.keys():
    print(f"The rivers are: {name}")
print("\n")
for country in rivers.values():
    print(f"the countries are: {country}")
print("---------------------------------------6.6 will start-----------------------------------------")

#6.6 去字典里查list里的值
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"YES, you are in {coder}")
    else:
        print(f"No,please register, {coder}")

print("---------------------------------------6.7 will start-----------------------------------------")

#6.7 把字典存到list里
people =[]
person = {'first_name': 'eric','last_name': 'matthes','age': 43,'city': 'sitka'   }
people.append(person)
person = {'first_name': 'kai','last_name': 'yao','age': 35,'city': 'BNE'   }
people.append(person)
print(people)  # 打印list
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")

print("---------------------------------------6.8 will start-----------------------------------------")
#6.8 把字典存到list里
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
    print(f"{name}'s owner is {owner}")  #print should be in for

print("---------------------------------------6.9 will start-----------------------------------------")

#6.9 在字典中存储list -- 要循环两次
favorite_places = {"kai":["Beijing","Hongkang"],"Julie":["AUS","USA","JAP"],"Andy":["FIJI"]} # 一个值如果可不用[]， 打印出来的是F - i - j- i
for name, places in favorite_places.items():  # 遍历字典要用.item(), keys() 或者values()
    if len(places) == 1:
        print(f"{name} likes this place:")
    else:
        print(f"{name} likes the following places")
    for place in places:
        print(f"- {place}")

print("---------------------------------------6.11 will start-----------------------------------------")
#6.11 字典里存字典 - 只循环一次
cities = {"Brisbane":{"Country":"Aus","population":12345,"fact":"Good"},
          "Beijing":{"Country":"China","population":123345,"fact":"many people"},
          "Sydney":{"Country":"Aus","population":1345,"fact":"Big city"}}
for city, city_info in cities.items():
    country = city_info["Country"]
    population = city_info["population"]
    fact = city_info["fact"]
    print(f"\n{city} is in {country}")
    print(f" -It has a population of {population}")
    print(f" -The fact is {fact}")



