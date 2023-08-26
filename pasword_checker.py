pasword=input("Enter the pasword to check : ")
D=0
L=0
U=0
Flag=0
lenth=len(pasword)
if(lenth>=8):
    for i in pasword:
        if(i.isdigit()):
            D=1
        elif(i.islower()):
            L=1
        elif(i.isupper()):
            U=1
        else:
            Flag=1
else:
    print("'The pasword must be 8 character are above'")
if(D==0 and U==0 and Flag==0):
    print("'Digit','Uppercase','Symbol' is missing")
elif(L==0 and D==0 and Flag==0):
    print("'Lowercase','Digit','Symbol' is missing")
elif(D==1 and U==0 and L==0 and Flag==0):
    print("'Upper','Lower','Symbol' is missing")
elif(D==0 and U==0 and L==0 and Flag==1):
    print("'Upper','Lower','digit' is missing")
elif(D==0):
    print("'Digit' is missing")
elif(U==0):
    print("'Uppercase',is missing")
elif(L==0):
    print("'Lowercase'is missing")
elif(Flag==0):
    print("'Symbol is missing")
else:    
    if(D==1 and L==1 and U==1 and Flag == 1):
        print("Strong pasword")
    else:
        print("Not strong") 
   
