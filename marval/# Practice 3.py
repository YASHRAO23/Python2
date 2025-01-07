# Practice 3

### Functions

# def my_function():
#     print("hello form a function")

## Calling a function
# my_function()


#######

from pyexpat import model


def my_function(fname):
    print(fname + " Refsnes")
    
my_function("Email")
my_function("Loby")
my_function("tita")


####  use * for unkown parameter

### you can also use key = value syntex

def my_function(child3, child2 ,child1):
    print("The yougest childe is" + child2)
    
my_function(child1="Yash", child2= " neha", child3="riya")

###### Pass statment

def my_function():
    pass


######### tri_recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


####  lambda function 

## Lambda arguments : expression

x = lambda a : a + 12
print(x(6))

x = lambda a , b : a*b
print(x(6,4))


######## Array

# an array can hold many valuse under single name
#you can acces the value using index number
car =["Valvo","BMW","Odi","jaguar","swift","harrier","safari","curve","BE6"]
x =car[4]
print(x)


########## Classes and objects ################
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = person("Kriti",32)
p1.age = 40
print(p1.name,p1.age)


# del p1.age

class car:
    def __init__(self,brand,price,model):
        self.brand = brand
        self.model = model
        self.price = price
        
c1 =car("BMW","2.3cr","M4")
print("I love this",c1.brand,"and this one comes under the price range of",c1.price,"and also this one",c1.model,"is my fav model")



######### 


def count_like_dislike(Nikhli,pranil):
    total_likes=0
    total_dislike=0
    
    for prefreacne in Nikhli:
        if prefreacne == "like":
            total_likes +=1
        elif prefreacne == "dislike":
            total_dislike += 1
    for prefreance in pranil:
        if prefreance == "like":
            total_likes +=1
        elif prefreacne =="dislike":
            total_dislike += 1
    
    return total_likes,total_dislike

movie = ["Rampage","kill","Maarco","Dangers khiladi","mission imposible 1","Calculate"]
Nikhil =["like","like","dislike","dislike","like","dislike"]
pranil =["dislike","like","like","like","dislike","like"]

like,dislike =count_like_dislike(Nikhil,pranil)
print(f"total like,{like}")
print(f"total dislike,{dislike}")
    


#######  polymorphism ############

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()