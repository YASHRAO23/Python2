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


# # print(f"Hello everyone i am YAsh but gusse who is with me my best{noun} rutuja")
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

operator = input("Enter the an operator(+ - * /):")

num1 = float(input("Enter the 1st number : "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+" :
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2 
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("your code is not working")
    