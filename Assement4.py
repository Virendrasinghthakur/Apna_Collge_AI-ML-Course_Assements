# Q1 create a bankaccount class with attributes accno,owner ,balance add methods to deposite ,withdraw and check balance

# class bankaccount:
#     def __init__(self,acc_no,owner_name,balance):
#         self.acc_no=acc_no
#         self.owner_name=owner_name
#         self.balance=balance
        
#     def deposit(self,amount):
#         # amount=int(input('enter the amount to deposite :'))
#         if(amount<=self.balance):
#             self.balance+=amount
#             print('transaction succesfull')
#         else:
#             print('please select a valid amoount !')
#         print('your account balacnce is',self.balance)
#     def withdraw(self,amount):
#         # amount=int(input('enter the amount to withdraw :'))
#         if(amount<=self.balance):
#             self.balance-=amount
#             print('transaction succesfull')
#         else:
#             print('account balance is too low !')
#         print('your account balacnce is',self.balance)
#     def check_balance(self):
#         print(f'your account balance is :{self.balance}')

# bank=bankaccount(2,'virendra',1500)
# bank.withdraw(500)


# Q2. create a class book with the following attributes titles,auther, list of reviews ans add methos to add new review , count reviews, display all reviews

# class book:
#     def __init__(self,title,author,reviews):
#         self.title=title
#         self.author=author
#         self.reviews=reviews
#     def add_a_review(self,review):
#         self.reviews.append(review)
#     def count_review(self):
#         print(f'total no of reviews are {len(self.reviews)}')
#     def display_all_review(self):
#         print(self.reviews)

# reviews=['its a good book','nice one','not too good','fine ']
# a=book('a good book','veersingh',reviews)
# a.add_a_review('quite good')
# a.count_review()
# a.display_all_review()

 
# Q3. create a class student with private attributes _name,_roll_no,_marks. provide getter and setter methods with validation(e.g marks cannot be nagative ,roll number has to be b/w 1&100 & name cannot be empty).

# class student:
#     def __init__(self,name,roll_no,marks):
#         self._name=name
#         self._roll_no=roll_no
#         self._marks=marks
#     def getter(self):
#         print(self._marks,self._name,self._roll_no)
#     def setter(self,marks):
#         self._marks=marks

# stu=student('veersingh',1234,45)
# stu.getter()
# stu.setter(82)
# stu.getter()
        

# Q4. create a class shape with a method area(). create subclasses circle,rectangle, and triangle that override the area() method.

# class Shape:
#     def area(self):
#         pass   # to be overridden by subclasses
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
# # execution layer
# shapes = [
#     Circle(5),
#     Rectangle(4, 6),
#     Triangle(10, 8)
# ]
# for shape in shapes:
#     print(f"Area: {shape.area()}")


# Q5.create a base class vehicle with the attributes like brand ,model. create two subclasses car and bike that add extra attributes -seat(in car) && engine_cc in bike

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc

# class Car(Vehicle):
#     def __init__(self, brand, model, seat):
#         super().__init__(brand, model)
#         self.seat = seat
        
# b=Bike('yamaha','r15',155)
# c=Car('toyota','innova',7)
# print(b.brand)

# create an abstract class employee with an abstract method clculate_salary(). create subclass intern,fulltimeemployee, and constract employee that implement the method diffrentely
# from abc import ABC ,abstractmethod
# class employee(ABC):
#     def __init__(self,name):
#         self.name=name
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class intern(employee):
#     def __init__(self,name,stipend):
#         super().__init__(name)
#         self.stipend=stipend
#     def calculate_salary(self):
#         return self.stipend
    
# class fulltimeemployee(employee):
#     def __init__(self,name,monthly_salary):
#         super().__init__()
#         self.monthly_salary=monthly_salary
#     def calculate_salary(self):
#         return self.monthly_salary

# class contractemployee(employee):
#     def __init__(self,name,hourlry_rate,hours_worked):
#         super().__init__(name)
#         self.hourly_rate=hourlry_rate
#         self.hours_worked=hours_worked
#     def calculate_salary(self):
#         return self.hourly_rate*self.hours_worked
    
# int=intern('veersingh',15000)
# print(int.calculate_salary())

# Q.7 create a class person that allows the constructor to work with: name only,name+age,name+age+address

# class person:
#     def __init__(self,name,age=None,address=None):
#         self.name=name
#         self.age=age
#         self.address=address

# p1=person('veersingh')
# p2=person('veersingh',21)
# p3=person('veersingh',21,'agra')

# print(p1.age)

# Q8. create a class player with ,a class variable player_count,instance variable name and level track how many players were created 

# class player:
#     player_count=0
#     def __init__(self,name,level):
#         self.name=name
#         self.level=level
#         player.player_count+=1

# p1 = player("Virendra", 5)
# p2 = player("Aman", 3)
# p3 = player("Riya", 7)

# print(player.player_count)   # 3

# Q9. create the following classes hebivores,carnivores,omnivores with attributes & methods . then create a class bear that inherits from all the above classes to showcase how multilple inheritance works
# class Herbivores:
#     def __init__(self):
#         pass
#     def eat_grass(self):
#         return "Eating grass 🌿"

# class Carnivores:
#     def __init__(self):
#         pass
#     def eat_meat(self):
#         return "Eating meat 🍖"

# class Omnivores:
#     def __init__(self):
#         pass
#     def eat_both(self):
#         return "Eating both plants and meat 🥗🍖"

# class Bear(Herbivores, Carnivores, Omnivores):
#     def __init__(self, name):
#         self.name = name
# b = Bear("Baloo")

# print(b.eat_grass())
# print(b.eat_meat())
# print(b.eat_both())

# Q10. let's create a chat system using oops cocepts.we have to create classes user,message,chatroom and we have to implement functions sending messages ,viewing chat history,user joining and leaving the chat room

class user:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    
class messages:
    def __init__(self,sender,content):
        self.sender=sender
        self.content=content
    def __str__(self):
        return f'{self.sender} : {self.content}'
    
class chatroom:
    def __init__(self,room_name):
        self.room_name=room_name
        self.users=[]
        self.messages=[]
    def join(self,user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user} joined {self.room_name}")
    
    def leave(self,user):
        if user in self.users:
            self.users.remove(user)
            print(f'{user} left {self.room_name}')
    
    def send_message(self,user,content):
        if user in self.users:
            print(f'{user} : {content}')
        else:
            print(f'{user} is not in {chatroom}!')
    
    def view_history(self):
        print(f'\n -- chat history in {self.room_name} __')
        for msg in self.messages:
            print(msg)

        
u1=user('virendra')
u2=user('gaji')

room=chatroom('general')

room.join(u1)
room.join(u2)

room.send_message(u1,'hii')
room.send_message(u1,'hello')

room.view_history()

room.leave(u2)