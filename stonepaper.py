import random
# print("rock=r")
# print("paper=p")
# print("scissor=s")


# computer=random.choice(['r','s','p'])
# print(computer)
# user=input("what is your choice : ")

# if user == computer:
#     print('Tie')
# elif((user=='p' and computer =='r') or (user=='s' and computer =='p') or (user=='r' and computer =='s')):
#     print("User won")    
# else:
#     print('user lost!')

def play():
    p=0
    while p == 0:

        user=input("Enter R or S or P : ").lower()
        
        comp=random.choice(['r','s','p'])
        print(comp)
        if user.lower() == comp:
            print('Tie')
        if win(user,comp):
            print('U won') 
        elif():    
            print('Ulost " :) " ')
        p=int(input("Do you want to continue enter:'0': "))    
    else:
        print("Hope u enjoy Thank u !!!")
        exit()
def win(useer,copl):
    useer.lower()
    #user coplayer
    if((useer=='p' and copl =='r') or (useer=='s' and copl =='p') or (useer=='r' and copl =='s')):
        return True

play()


















