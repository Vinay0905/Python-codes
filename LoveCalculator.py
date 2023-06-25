print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_name1=name1.lower()
lowercase_name2=name2.lower()
a=lowercase_name1.count("t") + lowercase_name2.count("t")
b=lowercase_name1.count("r") + lowercase_name2.count("r")
c=lowercase_name1.count("u") + lowercase_name2.count("u")
d=lowercase_name1.count("e") + lowercase_name2.count("e")
TRUE_LETTERS=str(a+b+c+d)

A=lowercase_name1.count("l") + lowercase_name2.count("l")
B=lowercase_name1.count("o") + lowercase_name2.count("o")
C=lowercase_name1.count("v") + lowercase_name2.count("v")
D=lowercase_name1.count("e") + lowercase_name2.count("e")


LOVE_LETTERS=str(A+B+C+D)
Love_score=int(TRUE_LETTERS+LOVE_LETTERS)

if Love_score<10 or Love_score>90:
    print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif Love_score>40 and Love_score<50:
    print(f"Your score is {Love_score}, you are alright together.")
else:
    print(f"Your score is {Love_score}.")
