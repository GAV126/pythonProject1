#8-1
def display_message():
    print("i am learning functions in this chapter")

#别和类混了，不用初始化实例。直接调用函数就行
#message = display_message()
display_message()
# if you add print, the result will add a None
# print(message)
print("----------------------8-2 will start---------------------------------------")

#8-2
def favorite_book(name):
    print(f"One of my favorite books is {name.title()}")

favorite_book("alice in wonderland")

print("----------------------8-3 will start---------------------------------------")

#8-3
def make_shirt(size,words):
    print(f"I am going to make a {size} t-shirt, which will print '{words}' on it")

make_shirt("large","I love Python")
make_shirt(words="Readability counts.", size='medium')

print("----------------------8-4 will start---------------------------------------")
#8-4
def make_shirt(size="large",words="I love BNE"):
    print(f"This is a {size} t-shirt. Print '{words}' on it")
make_shirt()
make_shirt("medium")
make_shirt("Small","I am a boy")

print("----------------------8-6 will start---------------------------------------")

def city_country(name, country):
    city  = f"\"{name},{country}\""
    return city
print(city_country("Beijing","China"))
print(city_country("Tokyo","Japan"))

print("----------------------8-7-1-not good will start---------------------------------------")

#8-7
def make_album(singer_name, album_name,num_song=None):
    dic = {"singer_name":singer_name,"album_name":album_name,"num_song":num_song}
    return dic
#print里调用函数,返回的是字典
print(make_album("Jasmine","courage"))
print(make_album("Taylor","1989",12))

print("----------------------8-7-2- better will start---------------------------------------")

def make_album(singer_name, album_name,num_song=None):
    if num_song:
       dic = {"singer_name":singer_name,"album_name":album_name,"num_song":num_song}
    else:
        dic = {"singer_name":singer_name,"album_name":album_name}
    return dic
print(make_album("Jasmine","courage"))
print(make_album("Taylor","1989",12))

print("----------------------8-7-3- answer will start---------------------------------------")

def make_album(singer_name, album_name,num_song=0):
    dic = {"singer_name": singer_name, "album_name": album_name}
    if num_song:
       dic["num_song"]=num_song
    return dic
print(make_album("Jasmine","courage"))
print(make_album("Taylor","1989",12))

print("----------------------8-8 will start---------------------------------------")

#8-8
def make_album(singer_name, album_name,num_song=0):
    dic = {"singer_name": singer_name, "album_name": album_name}
    if num_song:
       dic["num_song"]=num_song
    return dic

album_prompt = "\nWhat album are you thinking of:"
singer_prompt = "Who's the artist:?"

print("Enter 'quit' at any time to stop.")

while True:
    album_name= input(album_prompt) # must be here otherwise it will become forever loop
    if album_name =='quit':
        break
    singer_name = input(singer_prompt)
    if singer_name=='quit':
        break
    album = make_album(singer_name, album_name)
    print(album)
print("\nThanks for responding!")

print("----------------------8-9,8-10,8-11 will start---------------------------------------")
# move value from one list to the other

def show_message(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)

# show_message(["Hello","Welcome","Nihao","G'day"])  --- practice 8-9

def send_message(messages,sent_messages):
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hello","Welcome","Nihao","G'day"]
show_message(messages)
sent_messages = []
send_message(messages,sent_messages)
# 保留原list
# send_message(messages[:],sent_messages)
print("\nFinal Lists:")
print(messages)
print(sent_messages)

print("----------------------8-12 will start---------------------------------------")
def sandwich(*ingredients):
    if len(ingredients)==1:
        print("Please see the ingredient:")
    else:
        print("Please see the ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

sandwich("Onion","Olive","Meat","eggs")
sandwich("cheese","Cola")
sandwich("Subway")

print("----------------------8-14 will start---------------------------------------")
#不定数量的实参，是个字典。要把另外两个实参放进字典。
def  make_car(make, model,**options):
     car_dict = {"make":make.title(),"model" : model.title()}
     for option,value in options.items():
         car_dict[option] = value   # 给字典里添加值
         return car_dict
     # Option2: like P214
     # options["make"] = make
     # options["model"] = model
     # return options

my_outback = make_car("Toyota","Rav4",colour="grey",tow_bar=False) # 注意后两个参数是‘=’
print(my_outback)

my_compact = make_car("Toyota","Corolla",year=2021)
print(my_compact)

