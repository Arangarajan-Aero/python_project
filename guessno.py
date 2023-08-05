import random
a=int(input("Enter the no range"))
def randno(r):
    rand=random.randrange(1,r)
    guess=0
    while rand!=guess:
        guess=int(input("Enter the guessing no : "))
        if rand<guess:
            print("Sory you are too long")
        elif rand>guess:
            print("Sorry your guessed value is too short") 
    print(f"Haha successfully find the  value {rand}")           
randno(r=a)