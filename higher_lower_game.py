import random
from game_words import game
choice_A = random.choice(game)
choice_B = random.choice(game)
print(type(choice_A))
if choice_A == choice_B:
    choice_B == random.choice(game)
def formate_data(account):
    acc_name = account["name"]
    acc_country = account["country"]
    acc_followers = account["followers"]
    acc_occupation = account["occupation"]
    return f"The {acc_name} of {acc_country} is a {acc_occupation}"
def compare(acc_followersA,acc_followersB):
        if acc_followersA>acc_followersB:
            return "a"
        else:
            return "b"

acc_followersA = choice_A["followers"]
acc_followersB = choice_B["followers"]
mode = True
point = 0
while mode == True:
    
    print(f"COMPARE A::---> {formate_data(choice_A)}")
    print("                  Vs")
    print(f"COMPARE B::---> {formate_data(choice_B)}")
    answer = input("enter 'A' for choice_A or 'B' for choice_B--->")
    result = compare(acc_followersA,acc_followersB)   
    if result =="a":
         ret_value = choice_A
    else:
        ret_value = choice_B
    if answer != result:
        mode = False
        print(f"Game over your point is {point}")
        
    else:
        point +=1
        print(f"Your point is {point}")
        choice_A = ret_value
        choice_B = random.choice(game)
