import sys
user1=input("what's your name")
user2=input("what's your name")
user1_answer=input("%s,d you want to choose rock,paper,scissor" %user1)
user2_answer=input("%s do you want to choose rock,paper,scissor"%user2)
def compare(u1,u2):
    if(u1==u2):
        print("It's a tie")
    elif(u1=="rock"):
        if(u2=="scissor"):
            print("u1 won over u2 rock wins")
        else:
            print("u2 won over u1 scissor wins")
    elif(u1=="scissor"):
        if(u2=="paper"):
            print("scissor won over paper")
        else:
            print("paper won over scissor")
    elif(u1=="rock"):
        if(u2=="paper"):
            print("paper won over rock")
        else:
            print("rock won over paper")
    else:
        return ("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()
print(compare(user1_answer, user2_answer))

