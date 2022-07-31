print("Welcome To the Tech Quiz")
playing  = input("do you want to play? ")
if playing.lower() != "yes":
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

answer = input("full form of cpu? ")
if answer.lower() == "central proccesing unit":
    print('correct!')
    score+= 4
else:
    print('incorrect')
    score+= -1
#i am so lazy to add more question becouse its not thrilling 

#mark calculation
print("your mark is " + str(score/4) + " out of 2")