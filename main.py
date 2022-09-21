# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_ = name1.upper()
name2_ = name2.upper()
no_T = name1_.count("T")+name2_.count("T")
no_R = name1_.count("R")+name2_.count("R")
no_U = name1_.count("U")+name2_.count("U")
no_E = name1_.count("E")+name2_.count("E")
no_L = name1_.count("L")+name2_.count("L")
no_O = name1_.count("O")+name2_.count("O")
no_V = name1_.count("V")+name2_.count("V")
score1 = no_T+no_R+no_U+no_E
score2 = no_L+no_O+no_V+no_E
score = score1*10+score2
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
   print(f"Your score is {score}.")


