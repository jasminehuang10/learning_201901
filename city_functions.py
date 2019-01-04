'''import os
pwd=os.getcwd()
print(pwd)

print("hello world")

name="my name is jasmine"
print(name.upper())

first_name="jasmine"
last_name="huang"
full_name=first_name + " " + last_name
print("\tfull_name\n\t\tfull_name.capitalize()")

full_name_new=full_name.capitalize()
print(full_name_new)

import this
travel_destination=["taiwan","yunnan","niboer","eluosi","xinxilan"]
print(travel_destination)
print(sorted(travel_destination))
print(travel_destination)
print(sorted(travel_destination,reverse=True))
print(travel_destination)
travel_destination.reverse()
print(travel_destination)
travel_destination.reverse()
print(travel_destination)
travel_destination.sort()
print(travel_destination)
travel_destination.sort(reverse=True)
print(travel_destination)
print(len(travel_destination))


pizzas=["peigenpiz","tianyuanpiz","shuiguopiz"]
for pizza in pizzas:
    print("I like"+" "+pizza+"!")
print("I really like pizza!")


squares3=[value**3 for value in range(1,11)]
print(squares3)

#外星人颜色
alien_color="yellow"
if alien_color=="blue":
    print("you get 5 points")
elif alien_color=="yellow":
    print("you get 10 points")
elif alien_color=="red":
    print("you get 15 points")

#以特殊方式和管理员打招呼
user_list=["admin","jasmine","jone","peter","william"]
if user_list:
    for user in user_list:
        if user=="admin":
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello Eric,thank you for logging in again")
else:
    print("we need to fin some users")

#检查用户名
current_users=["Admin","jasmine","jone","peter","william"]
new_users=["admin","jasmine","henry","fiona","lisa"]
current_users=[current_user.lower() for current_user in current_users]
new_users=[new_user.lower() for new_user in new_users]
print(current_users)
for new_user in new_users:
    if new_user in current_users:
        print("pls key in other name")
    else:
        print("without user")


#序列
numbers=list(range(1,10))
for number in numbers:
    if number==1:
        numbers[0]="1st"
    elif number==2:
        numbers[1]="2nd"
    elif number==3:
        numbers[2]="3rd"
    else:
        numbers[number-1]=str(number)+"th"
for item in numbers:
    print(item)

#河流
river_country={"nile":"egypt","huanghe":"china","amazon":"brazil"}
for river,country in river_country.items():
    print("The " + river.title() + " runs through " + country.title() + "." )
for river in river_country.keys():
    print(river.title())
for country in river_country.values():
    print(country.title())

#关于人
personnal_info1={"first_name":"jasmine","last_name":"huang","age":24,
                "city":"shanghai"}
personnal_info2={"first_name":"fiona","last_name":"liu","age":25,
                "city":"shanghai"}
personnal_info3={"first_name":"peter","last_name":"zhang","age":28,
                "city":"guangzhou"}
personnal_info=[personnal_info1,personnal_info2,personnal_info3]
for i in personnal_info:
    print(i)

#喜欢的地方
favarite_places={
    "jasmine":["taiwan","niboer","yunnan"],
    "william":["xiangtan"],
    "jone":["beijing","shanghai"]
}
for name,cities in favarite_places.items():
    print("\n"+name.title()+" love places as bellow:")
    for city in cities:
        print(city.title())

#询问用餐人数
number=input("Pls input how many people have lunch:")
number=int(number)
if number > 8:
    print("Without spare table")
elif number <= 8:
    print("Have spare table")

#披萨
active= True
while active:
    ingrediant="pls input what you want to add:"
    ingrediant+="\nwhen you finish pls input quit."
    query=input(ingrediant)
    if query=="quit":
        active=False
    else:
        print("We will add " + query+ " for you.")


#披萨2
while True:
    ingrediant="pls input what you want to add:"
    ingrediant+="\nwhen you finish pls input quit."
    query=input(ingrediant)
    if query=="quit":
        break
    else:
        print("We will add " + query+ " for you.")

#三明治
print("pastrami sold out")
sandwich_orders=["pastrami","a","b","c","pastrami","pastrami"]
finished_sandwich=[]
for order in sandwich_orders:
    print("I made you " + order)
    finished_sandwich.append(order)
print(finished_sandwich)
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)
#城市名
def city_country(city,country):
    print('"'+city+','+country+'"')
city_country("shanghai","china")


#魔术师

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for name in names:
        name="the Great "+name
        show_magicians([name])

magicians=["a","b","c","d","e"]
make_great(magicians[:])
show_magicians(magicians)

#汽车
def make_car(manufacturer,model,**other_info):
    car={}
    car["manufacturer_name"]=manufacturer
    car["model_number"]=model
    for key,value in other_info.items():
        car["key"]=value
    return car
car=make_car("A","007",
         color="white",
         two_packages=True)
print(car)



import for_import
for_import.city_country("shanghai","china")

class User():
    """初始化属性"""
    def __init__(self,first_name,last_name,**others):
        self.first_name=first_name
        self.last_name=last_name
        self.others=others

    """打印用户信息摘要"""
    def describe_user(self):
        print("User name:"+self.first_name.title()+" "+self.last_name.title())

    """向用户发出个性化问候"""
    def greet_user(self):
        print("Hello,"+self.first_name.title()+" "+self.last_name.title())
user1=User("jasmine","huang")
user1.describe_user()
user1.greet_user()

#尝试登陆次数
class User():
    """初始化属性"""
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempt=0

    def increment_login_attempts(self):
        self.login_attempt+=1

    def reset_login_attempts(self):
        self.login_attempt=0

    """打印用户信息摘要"""
    def describe_user(self):
        print("User name:"+self.first_name.title()+" "+self.last_name.title())

    """向用户发出个性化问候"""
    def greet_user(self):
        print("Hello,"+self.first_name.title()+" "+self.last_name.title())
user1=User("jasmine","huang")
user1.increment_login_attempts()
print(user1.login_attempt)


#9-7管理员
class User():
    """初始化属性"""
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempt=0

    def increment_login_attempts(self):
        self.login_attempt+=1

    def reset_login_attempts(self):
        self.login_attempt=0

    """打印用户信息摘要"""
    def describe_user(self):
        print("User name:"+self.first_name.title()+" "+self.last_name.title())

    """向用户发出个性化问候"""
    def greet_user(self):
        print("Hello,"+self.first_name.title()+" "+self.last_name.title())
user1=User("jasmine","huang")
user1.increment_login_attempts()
print(user1.login_attempt)


class Admin(User):
    """管理员的独特之处"""
    def __init__(self,first_name,last_name):
        """初始化父类的属性"""
        super().__init__(first_name,last_name)
        self.priviliges=["can add post","can delete post","can ban user"]
    def show_priviledges(self):
        """显示管理员的权限"""
        for privilige in self.priviliges:
            print(privilige)
        #print(self.priviliges)
admin1=Admin("jasmine","huang")
admin1.show_priviledges()



#9-8权限
class User():
    """初始化属性"""
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempt=0

    def increment_login_attempts(self):
        self.login_attempt+=1

    def reset_login_attempts(self):
        self.login_attempt=0

    """打印用户信息摘要"""
    def describe_user(self):
        print("User name:"+self.first_name.title()+" "+self.last_name.title())

    """向用户发出个性化问候"""
    def greet_user(self):
        print("Hello,"+self.first_name.title()+" "+self.last_name.title())


class Priviliges():
    """一次模拟权限的简单尝试"""
    def __init__(self,priviliges=["can add post","can delete post","can ban user"]):
        self.priviliges=priviliges

    def show_priviledges(self):
        """显示管理员的权限"""
        for privilige in self.priviliges:
            print(privilige)
            # print(self.priviliges)

class Admin(User):
    """管理员的独特之处"""
    def __init__(self,first_name,last_name):
        """初始化父类的属性"""
        super().__init__(first_name,last_name)
        self.priviliges=Priviliges()

#实例化一个admin
admin1=Admin("jasmine","huang")
#调用admin权限
admin1.priviliges.show_priviledges()

#9-14骰子
from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self,times=1):
        self.times=times
        while times>0:
            x = randint(1, self.sides)
            print(x)
            times=times-1
die1=Die(10)
die1.roll_die(10)

#访客
active=True

while active:
    file_name = "test_new.txt"
    name = input("what you name?")
    if name != "q":
        with open(file_name, "a") as file_object:
            file_object.write(name + "\n")
    else:
        break

#加法运算
while True:
    try:
        number1 = int(input("first number:"))
        number2 = int(input("second number:"))
    except ValueError:
        warning = "we need numbers"
        print(warning)

    else:
        sum = number1 + number2
        print("sum is " + str(sum))
        break

#喜欢的数字
import json
favorite_number=input("you favorite number?")
with open("favorite_number.txt","a") as fn_file:
    json.dump(favorite_number,fn_file)
with open("favorite_number.txt") as fn_file:
    favorite_number=json.load(fn_file)
    print("I know your favorite number!It's "+favorite_number)

#课堂例子
import json
def get_stored_username():
    """如果储存了用户名就获取它"""
    filename="username.json"
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username=input("what is your name?")
    filename="username.json"
    with open(filename,"w") as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username=get_stored_username()
    if username:
        print("Welcome back,"+username+"!")
    else:
        username=get_new_username()
        print("We will remember you when you come back,"+username+"!")
greet_user()

#11-2人口数量
def city_country(city,country,population):
    city_country = city.title()+","+country.title()+"-population "+str(population)
    print(city_country)
    return city_country

city_country("jasmine","huang",100)'''

#11-3雇员
class Employee:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def give_raise(self,salary=5000):
        self.salary=salary
        print(self.first_name,self.last_name,self.salary)

employee=Employee("jasmine","huang")
employee.give_raise()
