import random
birthYr = input("enter your birth year: ")
int(birthYr)
age = 2022 - int(birthYr)
print( "I am " + str(age)+  " years old!")
if age>=19:
    num = random.randint(0,10)
    print("I'm going to buy " + str(num) + " loterry tickets!")
else:
    print('I am too young')
wrong = True
lottery = random.randint(0,10)
print(lottery)
guess = int(input("What is you lucky guess? "))
while True:
    if guess != lottery:
        if lottery <= 5:
            print("hint: the number is within 0 to 5!")
            guess = int(input("What is you lucky guess? "))
        elif lottery > 5:
            print("hint: the number is between 6 and 10!")
            guess = int(input("What is you lucky guess? "))
        print("try again ")
    else:
        print("good job")
        break

