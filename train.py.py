import random
import datetime

print("Trichy-coimbatore")
#print("Trichy-madurai")

#enter the arrival station
Arival=input("Enter the arival station name")
#destination station name
Dest=input("Enter the destination")
if Arival=="trichy" or "Trichy" and Dest=="coimbatore" or "Coimbatore":
    print("Train timing")
    print("3.00Am Press 1")
    print("6.00Am Press 2")
    print("1.00Pm Press 3")
    Time=int(input("Enter the choice"))
    if Time==1:
        pass_count=int(input("Enter the pass_count"))
        pass_list=[]
        T_date=datetime.datetime.now()
        for i in range(pass_count):
            pass_Nm=input(f"Enter name: ")
            pass_age=int(input("Enter Age "))
            pass_seat=input(f"Enter lower or upper")
            seat_no=random.randint(1,50)
            pass_list.append(pass_Nm)
            pass_list.append(pass_age)
            pass_list.append(pass_seat)
            pass_list.append(seat_no)
            for j in pass_list:
                print(f"date :{T_date}")
                print(f"Name :{pass_Nm} seat No: {seat_no} seatType : {pass_seat}")
                
                break
                
    
                    
            
        #print(pass_list)
            
            
    
