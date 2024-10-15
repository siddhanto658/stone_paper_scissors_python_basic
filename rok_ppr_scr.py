import random as rd
# rock = 1
# paper = 0
# scissor = -1
man_inp=(input("Enter your choice R / P / S : "))
man_cho=man_inp.lower()
print(man_cho)
comp=rd.choice([-1,0,1])
#input part is done , 2 values are collected 
#one by the user and one by computer

youDict={
    "r":1,
    "p":0,
    "s":-1
}
revDict={
    1 :"Rock",
    0 :"Paper",
    -1:"Scissors"
}
man=youDict[man_cho] #prints the choices, to make the game fair.
print(f"You chose : {revDict[man]} , \n Computer Chose : {revDict[comp]}")

#all possible outcomes

if (comp==man):
    print("It's a Draw !!!")

else:
    if(comp==1 and man==0):
        print("Congratulations!! You won !")
    elif(comp==0 and man==1):
        print("You lose :( .")
    elif(comp==1 and man==-1):
        print("You lose :( .")
    elif(comp==-1 and man==1):
        print("Congratulations!! You won !")
    elif(comp==0 and man==-1):
        print("Congratulations!! You won !")
    elif(comp==-1 and man==0):
        print("You lose :( .")
    else:
        print("something went wrong ~~")
