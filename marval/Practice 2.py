##### 2D collections ##########

# fruits = {"apple","banana","orange","cetaphal"}
# vegitables = ["cabages","mushrooms","tomato","batata"]
# meats =["chicken","fish","tandori","tikka"]

# groceries =[fruits,vegitables,meats]

# for category in groceries:
#     for fruits in category:
#         print(fruits, end=" ")
#     print()
        
        
######### 2D tuple ########

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))

# for row in num_pad:
#     for num in row:
#         print(num, end="")
#     print()
        
        
############ Quiz game ###########

question =(("Which one is your fav anime? :"),
           ("which one is your fav  charactor? :"),
           ("which one power you wish you can have in real life? :"),
           ("Which one is best anime girl charactor? :"),
           ("Tell me episod number you want to repeadted daily? :"))

options = (("A.one piece","B.Nauroto","C.Solo leveling","D.jijutsu"),
           ("A.Kakashi","B.Naruto","C.levi","D.itachi"),
           ("A.rasingan","B.chakara","C.lighting strike","D.telepoart"),
           ("A.Henata","B.sakura","C.liya","D.kriya"),
           ("A.225","B.336","C.55","D.08"))

answers = ("C", "A", "C", "A", "D")

guesses = []
score = 0
question_num = 0


for question in question:
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guesses == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]}")
        question_num += 1