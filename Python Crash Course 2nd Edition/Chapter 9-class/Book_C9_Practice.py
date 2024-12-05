#9-1 restaurant,

class Resutaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"the restaurant name is {self.restaurant_name}, and its dishes is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}  is open")

restaurant = Resutaurant("VP Chinese","Chinese")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("--------------------------------------#9.4 will start-----------------------------------------------------")


# 9-4
class Resutaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served =0
    def describe_restaurant(self):
        print(f"the restaurant name is {self.restaurant_name}, and its dishes is {self.cuisine_type}")
        print(f"So, there are {self.number_served} people come here.")
    def set_number_served(self,number):
        if number <0:
            print(f"you cannot enter a value less than 0")
        else:
            self.number_served = number
            print(f"Now,the number of customer is {self.number_served}")
    def increment_number_served(self, increment):
        if increment <0:
            print(f"you cannot enter a value less than 0")
        else:
            self.number_served += increment
            print(f"Now,after increment, the number of customer is {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}  is open")

restaurant = Resutaurant("VP Chinese","Chinese")

restaurant.describe_restaurant()
restaurant.set_number_served(123)
restaurant.increment_number_served(100)
restaurant.open_restaurant()
print("--------------------------------------#9.6 will start-----------------------------------------------------")

#9.6
class IceCreamStand(Resutaurant):
    def __init__(self,restaurant_name, cuisine_type="ice-cream"):  # add a default value
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []  # add flavours attribute here, and it is a list

    def show_icecream(self):
        print(f"we have the following flavours:")
        for flavour in self.flavours:
            print(f"- {flavour}")

big_one = IceCreamStand("DQ") #初始化实例对象
big_one.describe_restaurant()
big_one.flavours = ["Vanila","banana","berry"]  # 调用flavours 对象并赋值
big_one.show_icecream()
print("--------------------------------------#9.3 will start-----------------------------------------------------")

#9-3
class User:
    def __init__(self,first_name, last_name,username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username =username
        self.email = email
        self.location = location
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} 's username is {self.username}")
    def greet_user(self):
        print(f"Welcome,{self.first_name} {self.last_name} ")

admin = User("kai","yao","Kaiy","kai.y@123.com","BNE")
admin.describe_user()
admin.greet_user()
print("--------------------------------------#9.7 will start-----------------------------------------------------")

#9.7
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges=[]
    def show_privileges(self):
        if self.privileges:   # 判断是否有管理权限
            for privilege in self.privileges:
                print(f"Admin {self.first_name} {self.last_name} has the following privileges:")
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

ad = Admin("kai","yao","Kaiy","kai.y@123.com","BNE")
ad.privileges = ["can add post","can delete post","can ban user"]
ad.describe_user()
ad.show_privileges()
print("--------------------------------------#9.8 will start-----------------------------------------------------")

#9.8
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges() #Privileges 类在下边


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges() #Admin类的实例(eric)去访问Privileges类里的方法

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()

print("--------------------------------------#9.13 will start-----------------------------------------------------")
from random import randint
class Dice:
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self):
        return randint(1,self.sides)
# Make a 6-sided die, and show the results of 10 rolls.
d6 = Dice() # default value is 6
results=[]
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result) #Return a number between 1 and the number of sides
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Dice(20)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
shape = int(input("How many sides?"))
times = int(input("How many times"))
d10 = Dice(shape)
results = []
for roll_num in range(times):
    result = d10.roll_die()
    results.append(result)
print(f"\n{times} rolls of a {shape}-sided die:")
print(results)

print("--------------------------------------#9.14 will start--------------------------------------------------------")

from random import choice
possibilities =["10","1","2","3","4","5","6","7","8","9","a","b","c","d","e"]
winning_ticket = []
print("Let's see the winning ticket is... ")
while len(winning_ticket)<4:
    pulled_item = choice(possibilities )
    if pulled_item  not in winning_ticket:
        print(f"We pull a {pulled_item}")
        winning_ticket.append(pulled_item)
print(f"The final winning ticket is {winning_ticket}")

print("--------------------------------------#9.15 will start--------------------------------------------------------")

from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 10000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")




