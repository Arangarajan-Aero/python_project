import random
def cguess(): 
    given_no=int(input("Enter the no so comp can guess : "))
    random_no=random.randint(1,20)
    if given_no != random_no:
        if given_no < random_no:
            while given_no < random_no:
                print("if",random_no)
                random_no=random_no-1
        elif given_no > random_no:
            while given_no < random_no:
                print("else",random_no)
                random_no=random_no+1
    print(f"Haha don't mess me i am a computer ur gven no is {random_no} ")
cguess()
