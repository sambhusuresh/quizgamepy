print("Welcome To the Tech Quiz")
playing  = input("do you want to play? ")
if playing != "yes":
    quit()
print("Okay! Let's play :) ")
score = 0 
answer = input("full form of RAM? ")
if answer.lower() == "random acces memmory":
    print('correct!')
    score+= 4
else:
    print('incorrect')
    score+= -1
    #negetive marking
