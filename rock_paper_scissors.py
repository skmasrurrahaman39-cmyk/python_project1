
import random

print ("1 for Rock\n 2 for Paper\n 3 for Scissors")
computer = random.choice([1,2,0])


game =input("Enter your choice: ")
gamedict = {"s":1, "p":2, "r":0}
you = gamedict[game]

reverseddict ={0: "Rock", 1: "Paper", 2: "Scissors"}

print(f"your choice: {reverseddict[you]} \ncomputer chouce: {reverseddict[computer]}")


if(computer ==1 and you ==1):
    print("its a ---draw---")

elif(computer ==2 and you ==2):
    print("its a ---draw---")

elif(computer ==0 and you ==0):
    print("its a ---draw---")

else:                                          # 0 for Rock      1 for Paper            2 for Scissors
    if(computer ==1 and you ==2 ):
        print("you are \*\*\ win /*/*/")

    elif(computer ==1 and you ==0):
        print("you are  LOSE!")
        
    elif(computer ==2 and you ==1):
        print("you are LOSE!")

    elif(computer ==2 and you ==0):
        print("you are \*\*\ win /*/*/")

    elif(computer ==0 and you ==1):
        print("you are \*\*\ win /*/*/")

    elif(computer ==0 and you ==2):
        print("you are LOSE!")

    else:
        print("something is worng x")



    