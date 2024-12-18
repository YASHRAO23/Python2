##### 2D collections ##########

# fruits = {"apple","banana","orange","cetaphal"}
# vegitables = ["cabages","mushrooms","tomato","batata"]
# meats =["chicken","fish","tandori","tikka"]

# groceries =[fruits,vegitables,meats]

# for category in groceries:
#     for fruits in category:
#         print(fruits, end=" ")
#     print()
        
        
# ######### 2D tuple ########

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))


# for row in num_pad:
#     for num in row:
#         print(num, end="")
#     print()
        
        
############ Quiz game ###########

# questions =(("Which one is your fav anime? :"),
#            ("which one is your fav  charactor? :"),
#            ("which one power you wish you can have in real life? :"),
#            ("Which one is best anime girl charactor? :"),
#            ("Tell me episod number you want to repeadted daily? :"))

# options = (("A.one piece","B.Nauroto","C.Solo leveling","D.jijutsu"),
#            ("A.Kakashi","B.Naruto","C.levi","D.itachi"),
#            ("A.rasingan","B.chakara","C.lighting strike","D.telepoart"),
#            ("A.Henata","B.sakura","C.liya","D.kriya"),
#            ("A.225","B.336","C.55","D.08"))

# answers = ("C", "A", "C", "A", "D")

# user_guesses = []
# user_score = 0
# question_num = 0


# for question in questions:
#     print("-------------------------------")
#     print(question)
#     for option in options[question_num]:
        
#         print(option)
        
#     guess = input("Enter (A, B, C, D): ").upper()
#     user_guesses.append(guess)
#     if user_guesses == answers[question_num]:
#         user_score +=1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]}")
#         question_num += 1

# print("answers : ",end="")       
# for answer in answers:
#     print(answers,end=" ")
# print()

# print("user_guesses : ",end="")       
# for guess in user_guesses:
#     print(guess,end=" ")
# print()


# score = int(user_score / len(questions) * 100)
# print(f"Your score is : {score}%")





################ updated version of quiz code ########################

# def display_question(question: str, options: tuple) -> None:
#     """Display a question and its options."""
#     print("-------------------------------")
#     print(question)
#     for option in options:
#         print(option)

# def get_user_guess() -> str:
#     """Get the user's guess."""
#     while True:
#         guess = input("Enter (A, B, C, D): ").upper()
#         if guess in ["A", "B", "C", "D"]:
#             return guess
#         else:
#             print("Invalid input. Please enter A, B, C, or D.")

# def calculate_score(user_guesses: list, answers: tuple) -> int:
#     """Calculate the user's score."""
#     score = sum(1 for guess, answer in zip(user_guesses, answers) if guess == answer)
#     return int(score / len(answers) * 100)

# def main() -> None:
#     """Run the quiz game."""
#     questions = (
#         "Which one is your fav anime? :",
#         "which one is your fav  charactor? :",
#         "which one power you wish you can have in real life? :",
#         "Which one is best anime girl charactor? :",
#         "Tell me episod number you want to repeadted daily? :"
#     )

#     options = (
#         ("A.one piece", "B.Nauroto", "C.Solo leveling", "D.jijutsu"),
#         ("A.Kakashi", "B.Naruto", "C.levi", "D.itachi"),
#         ("A.rasingan", "B.chakara", "C.lighting strike", "D.telepoart"),
#         ("A.Henata", "B.sakura", "C.liya", "D.kriya"),
#         ("A.225", "B.336", "C.55", "D.08")
#     )

#     answers = ("C", "A", "C", "A", "D")

#     user_guesses = []
#     for question, options in zip(questions, options):
#         display_question(question, options)
#         guess = get_user_guess()
#         user_guesses.append(guess)
#         if guess == answers[questions.index(question)]:
#             print("CORRECT!")
#         else:
#             print("INCORRECT!")
#             print(f"{answers[questions.index(question)]}")

#     print("answers : ", end="")
#     for answer in answers:
#         print(answer, end=" ")
#     print()

#     print("guesses : ", end="")
#     for guess in user_guesses:
#         print(guess, end=" ")
#     print()

#     score = calculate_score(user_guesses, answers)
#     print(f"Your score is : {score}%")

# if __name__ == "__main__":
#     main()

###############  dictionaries ############

# capitals = {"USA" : "washington DC",
#             "INDIA": "Delhi",
#             "Russia": "moscow",
#             "China" : "Biljing"}

# print(capitals.get("USA"))

########### Array ###########

Monthly_expense = ["January : 2200","February : 2350","March : 2600","April : 2130","May : 2190"]

### 1)In Feb, how many dollars you spent extra compare to January? 
January_expense = int(Monthly_expense[0].split(": ")[1])
Februray_expense = int(Monthly_expense[1].split(": ")[1])

extra_spent = Februray_expense - January_expense
print(f"In february, you spent {extra_spent} dollars extra compared to january")

### 2)Find out your total expense in first quarter (first three months) of the year.
January_expense = int(Monthly_expense[0].split(": ")[1])
February_expense = int(Monthly_expense[1].split(": ")[1])
March_expense = int(Monthly_expense[2].split(": ")[1])

first_quarter_total = January_expense + February_expense + March_expense
print(f"Your total expense in first quarter is {first_quarter_total} dollars")

##### 3)Find out if you spent exactly 2000 dollars in any month
# Monthly expenses list
Monthly_expense = ["January : 2200", "February : 2350", "March : 2600", "April : 2130", "May : 2190"]

# Check if any month has an expense of exactly 2000 dollars
found = False
for month in Monthly_expense:
    expense = int(month.split(": ")[1])  # Extracting the expense amount
    if expense == 2000:
        found = True
        print(f"You spent exactly 2000 dollars in {month.split(':')[0]}.")
        break

if not found:
    print("You did not spend exactly 2000 dollars in any month.")
### 4)You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
#Current_April_expense
April_expense = int(Monthly_expense[3].split(": ")[1])  # Extracting the expense for April
April_expense -= 200  # Subtracting the refund

#Updating the Monthly_expense list
Monthly_expense[3] = f"April : {April_expense}"  # Updating the April expense

print(Monthly_expense)  # Display the updated monthly expenses

### 5)June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
Monthly_expense.insert(5,"June : 1980")
                        
print(Monthly_expense)


################ You have a list of your favourite marvel super heros.#####################
heros=['spider man','Thor','Hulk','Iron man','Captain america']

length = len(heros)
print(length)

## Add 'black panther' at the end of this list

heros.append("Black panther")
print(heros)

### You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'

heros.remove("Black panther")
print(heros)

heros.insert(3,"Black panther")
print(heros)

#####Now you don't like thor and hulk because they get angry easily :)So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#Do that with one line of code.


heros[1:3]=["Doctor strange"]
print(heros)

heros.sort()
print(heros)
