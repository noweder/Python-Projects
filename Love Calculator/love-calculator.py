print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

T = lower_name1.count("t") + lower_name2.count("t")
R = lower_name1.count("r") + lower_name2.count("r")
U = lower_name1.count("u") + lower_name2.count("u")
E = lower_name1.count("e") + lower_name2.count("e")
true = T + R + U + E 

L = lower_name1.count("l") + lower_name2.count("l")
O = lower_name1.count("o") + lower_name2.count("o")
V = lower_name1.count("v") + lower_name2.count("v")
E = lower_name1.count("e") + lower_name2.count("e")
love = L + O + V + E 

love_score = true*10 + love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else: 
    print(f"Your score is {love_score}.")
    