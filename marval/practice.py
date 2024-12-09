# # # """
# # # str1 = ("this are my first string ")
# # # str2 = ("This is the on my best")
# # # print(str2)

# # # items = ["Google","yaahoo","microsoft",3,4]
# # # items [0] = "YASH"
# # # items [3] = "RAo"
# # # items [4] = "KK"
# # # items.append("MMM")
# # # items.extend("raooo")
# # # items.insert(3,"Rutuja")
# # # #items.pop(2)
# # # print(items)


# # # dict1 = {}

# # # dict1["rutuja"] = 100
# # # print(dict1)
# # # dict2 ={}
# # # dict2["YASH"] = 100
# # # dict2["RUTUJA"] = 100 
# # # print(dict2)
# # # dict3 ={}
# # # dict2["riya"] = 100
# # # print(dict3)

# # # a = 5jhljkj
# # # b =10

# # # c = "Rutuja"
# # # print(c)

# # # print (str(a)+str(b)+ c)

# # # print("10 - 5 is", 10-5)
# # # print("10 * 5 is",10*5)
# # # print("10 / 5 is",10/5)
# # # print("10 % 5 is",10%5)

# # # var = int(input())
# # # print(var)

# # # #var = str(input())
# # # #print(var)

# # # if (var > 4):
# # #     print("greater than 4")
# # # elif(var==2):
# # #     print("equal to 2")

# # # else:
# # #     print("smaller than 4")

# # # 

# # # for i in range(101,151):
# # #     print(i)

# # #f = open("te","w")
# # #f.write("subsxribe to my channel")
# # #f.close()

# # ##matlips games 
# # ## fill in the blanks 
# # noun = input(("word"))
# # adjective1 = input(("name"))
# # adjective2 = input(("name"))


# # print(f"Hello everyone i am YASH but gusse who is with me my best{noun} rutuja")
# # print(f"we are going on date today in pune cafe name is {adjective1} you guys are know i think")
# # print(f"so what do you think i can propes her or not {adjective2}.ok")
# # print(f"that's why i a happy ")

# age = 24

# print(f"you are {age} year old")

# # Typecasting :- the process of converting a variable from one data type to another one data tyoe

# name = "YASH RAO"
# age = 25
# gpa = 6.45
# is_student = True

# # print(type(name))
# # print(type(age))
# # print(type(gpa))
# # print(type(is_student))

# # age = float(age)
# # print(age)

# # gpa =int(gpa)
# # print(gpa)

# # name =int(name)
# # print(name)

# ### exercise 1 reactangle area calc

# length = int(input("Enter the length:"))
# width = int(input("Enter the width:"))

# area = length * width
# print(f"the area is :{area}cm²")

#####       Day 2     ###############
##operators

# import math
# radius = float(input("Enter the radius of a circle : "))

# cicumference = 2 * math.pi * radius

# print(f"The cicumferance is : {cicumference}")

# import math

# radius =float(input("Enter the radius of circle : "))

# area = math.pi * pow(radius,2)
# print(f"the area of circle is {area}")

# a = float(input("Enter side A : "))
# b = float(input("Enter side B : "))

# c = math.sqrt(pow(a,2) + pow(b,2))
# print(f"The length of hypotenuse is {c}")


# age = int(input("Enter the age : "))
 
# if age>=5:
#     print("you are eligible for school")
# else:
#     print("you are not eligible for school")


# dairy = False

# if dairy:
#     print("diary is open")
# else:
#     print("dairy is colsed")
    
## Python Calculator

# operator = input("Enter the an operator(+ - * /):")

# num1 = float(input("Enter the 1st number : "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+" :
#     result = num1 + num2
#     print(result)
# elif operator == "-":
#     result = num1 - num2 
#     print(result)
# elif operator == "*":
#     result = num1 * num2
#     print(result)
# elif operator == "/":
#     result = num1 / num2
#     print(result)
# else:
#     print("your code is not working")
    
    
##### Python weight converter #########

# weight =float(input("Enter your weight : "))
# unit = input("Enter unit Kilogram or Pounds ? (K or P):")

# if unit == "k":
#     weight = weight * 2.205
#     unit ="Lbs."
#     print(f"Your weight is : {round(weight)}{unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is : {round(weight)}{unit}")
# else:
#     print(f"{unit} was not valid")
    
    

########### Tempreature Converstion program #########

# unit = input("Is temprature in Celsiuse or Fahrenheit (C/F) : ")
# temp = float(input("Enter the tepresture : "))

# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temprature in Fahrenheit is : {temp} °F ") 
# elif unit == "F":
#      temp = round((temp - 32) * 5 / 9, 1)
#      print(f"The temprature in Celcius is : {temp} °C ")
# else:
#     print(f"{unit} is an invalid unit temprature ")
    
    
    
    
############ logical Operators ############

# Evaluate multiple conditions(or, and , not)
# or = at least one conditon must be True
# and= both conditionos must be True
# not= inverts the conditions (not False, not True)


# temp = 0
# is_sunny = True

# if temp >= 28 or is_sunny:
#     print("It is Hot outside 🥵")
#     print("it is sunny 🌞")
# elif temp <= 0 and is_sunny:
#     print("It is Cold outside 🥶") 
#     print("It is sunny🌞")
# elif 28 > temp > 0 and  is_sunny:
#     print("It is WARM outside 😊")
#     print("It is sunny 🌞")
# elif temp >= 28 and not is_sunny:
#     print("It is Hot outside 🥵")
#     print("it is cloudy ⛅ ")
# elif temp <= 0 and not is_sunny:
#     print("It is Cold outside 🥶") 
#     print("It is cloudy ⛅")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is WARM outside 😊")
#     print("It is cloudy ⛅")  



########  Conditional Expression ##########
# a one line short-cut for if else statement(ternary operator)
# print or asing one of two value based on conditions 
# X if condition else Y


# num = 1

# a = 6
# b = 7
# age = 22

# temp = -8
# print("Greater") if num > 5 else print("Lesser")
# max_num = a if a > b else b
# min_num = a if a < b else b

# print(max_num)
# print(min_num)

# print("Positive"  if num > 5 else "Nigative")

# result = ("Even" if num % 2 == 0 else "ODD")
# print(result)


# status = "adult" if age >= 18 else "child"
# print(status)

# wether = ( "Hot🌞"if temp >= 0 else "cold🥶")
# print(wether)
 
 
##### string methods ######

# name = input("Enter your full name : ")

#result = len(name)
#result = name.find("C")
#result = name.rfind("C")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result =phone_number.count("-")
# phone_number =phone_number.replace("-"," ")

# print(phone_number)


result = help(str)
print(result)