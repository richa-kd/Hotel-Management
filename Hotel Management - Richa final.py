import random
import string
import csv


print("Welcome to Hotel Marbella")
print("")

L=[]
name=input("Enter Your Full Name: ")
L.append(name)
phone=str(input("Enter Your Phone Number: "))
L.append(phone)
checkin=str(input("Enter the Check In Date(DD-MM-YYYY): "))
L.append(checkin)
checkout=str(input("Enter the Check Out Date(DD-MM-YYYY): "))
L.append(checkout)
print("")

print("Please Choose a Room.")
print("These Are the Available Room Options:")
print("Option 1. Room A (1 bed) - Rs. 3000")
print("Option 2. Room B (2 beds) - Rs. 4000")
print("Option 3. Room C (3 beds) - Rs. 5000")
print("Option 4. Room D (4 beds) - Rs. 6000")
print("")

x=int(input("Please Enter Your Desired Option Number: "))
roomcost=0
n=0
var=0
no1=0
no2=0
no3=0
no4=0
while var==0:
 if(x==1):
    n=0
    n=int(input("How Many Rooms Would You Like? "))
    y=int(input("How many nights? "))
    no1+=n
    ch1=3
    if no1>3:
        print("Not enough rooms available, please choose another")
        print("Number of rooms available:",ch1-(no1-n))
        no1=no1-n
        x=int(input("Please Enter Your Desired Option Number: "))
        continue
    else:
        print("After Opting for Room A, Your Final Room(s) Cost Comes to Rs.", roomcost+(3000*y*n))
        roomcost=roomcost+(3000*y*n)
        n=0
        hello=input("Would you like to choose more rooms?(Yes/No) ")
        if hello=="Yes":
            x=int(input("Please Enter Your Desired Option Number: "))
        else:
            var=1
 elif(x==2):
    n=0
    n=int(input("How Many Rooms Would You Like? "))
    y=int(input("How many nights? "))
    no2+=n
    ch2=3
    if no2>3:
        print("Not enough rooms available, please choose another")
        print("Number of rooms available:",ch2-(no2-n))
        no2=no2-n
        x=int(input("Please Enter Your Desired Option Number: "))
        continue
    else:
        print("After Opting for Room B, Your Final Room(s) Cost Comes to Rs.", roomcost+(4000*y*n))
        roomcost=roomcost+(4000*y*n)
        n=0
        hello=input("Would you like to choose more rooms?(Yes/No) ")
        if hello=="Yes":
            x=int(input("Please Enter Your Desired Option Number: "))
        else:
            var=1
 elif(x==3):
    n=0
    n=int(input("How Many Rooms Would You Like? "))
    y=int(input("How many nights? "))
    no3+=n
    ch3=3
    if no3>3:
        print("Not enough rooms available, please choose another")
        print("Number of rooms available:",ch3-(no3-n))
        no3=no3-n
        x=int(input("Please Enter Your Desired Option Number: "))
        continue
    else:
        print("After Opting for Room C, Your Final Room(s) Cost Comes to Rs.", roomcost+(5000*y*n))
        roomcost=roomcost+(5000*y*n)
        n=0
        hello=input("Would you like to choose more rooms?(Yes/No) ")
        if hello=="Yes":
            x=int(input("Please Enter Your Desired Option Number: "))
        else:
            var=1
 elif(x==4):
    n=0
    n=int(input("How Many Rooms Would You Like? "))
    y=int(input("How many nights? "))
    no4+=n
    ch4=3
    if no4>3:
        print("Not enough rooms available, please choose another")
        print("Number of rooms available:",ch4-(no4-n))
        no4=no4-n
        x=int(input("Please Enter Your Desired Option Number: "))
        continue
    else:
        print("After Opting for Room D, Your Final Room(s) Cost Comes to Rs.", roomcost+(6000*y*n))
        roomcost=roomcost+(6000*y*n)
        n=0
        hello=input("Would you like to choose more rooms?(Yes/No) ")
        if hello=="Yes":
            x=int(input("Please Enter Your Desired Option Number: "))
        else:
            var=1
 else:
    print("Please Choose Either Option 1, 2, 3 or 4")
print("")

amenities=input("Would You Like to See Our Walk-In Entertainment Amenities?(Yes/No) ")
x=0
print("")

if(amenities=="Yes"):
    number=0
    amenitiescost=0
    while number==0:
        print("Option 1. Spa - Rs. 500 Per Person")
        print("Option 2. Bowling - Rs. 80 Per Game")
        print("Option 3. Table Tennis - Rs. 60 Per Person for 30 mins")
        print("Option 4. Mini Golf Course - Rs. 80 Per Person")
        print("Option 5. Swimming Pool - Rs. 50 Per Person for 2 hours")
        print("Option 6. None")
        print("")
        x=int(input("Please Choose Your Desired Option Number: "))

        if(x==1):
            people=0
            people=int(input("How Many People in Total? "))
            print("After Opting for Spa, Your Spa Cost Comes to Rs.",500*people)
            amenitiescost+=500*people
            print("")
        
            ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
            if(ask=="Yes"):
                number=0
            else:
                number=1
            print("")

        elif(x==2):
            people=0
            people=int(input("How Many People in Total? "))
            n=0
            n=int(input("How Many Games Would You Like PER PERSON? "))
            print("After Opting for Bowling, Your Bowling Cost Comes to Rs.", 80*people*n)
            amenitiescost+=80*people*n
            print("")
        
            ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
            if(ask=="Yes"):
                number=0
            else:
                number=1
            print("")
        
        elif(x==3):
            people=0
            people=int(input("How many people for table tennis? "))
            n=0
            n=int(input("How Many Rounds of 30mins Would You Like PER PERSON? "))
            print("After Opting for Table Tennis, Your Table Tennis Cost Comes to Rs.", 60*people*n)
            amenitiescost+=60*people*n
            print("")

            ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
            if(ask=="Yes"):
                number=0
            else:
                number=1
            print("")
        
        elif(x==4):
            people=0
            people=int(input("How Many People in Total?"))
            print("After Opting for Mini Golf Course, Your Mini Golfing Cost Comes to Rs.", 80*people)
            amenitiescost+=80*people
            print("")
        
            ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
            if(ask=="Yes"):
                number=0
            else:
                number=1
            print("")

        elif(x==5):
            people=0
            people=int(input("How Many In Total? "))
            n=0
            n=int(input("How Many Rounds of 2 Hours would you like PER PERSON? "))
            print("After Opting for Swimming Pool, Your Swimming Pool Cost Comes to Rs.", 50*people*n)
            amenitiescost+=50*people*n
            print("")
        
            ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
            if(ask=="Yes"):
                number=0
            else:
                number=1
            print("")

        elif(x==6):
            number=1
        else:
            print("Please Choose Either Option 1, 2, 3, 4, 5 or 6")
            print("")
else:
    amenitiescost=0

breakfastcost=0
bf=input("Will You Be Having Breakfast by the Hotel for Rs. 250 PER DAY?(Yes/No) ")
print("")

if(bf=="Yes"):
    people=int(input("How Many People In Total? "))
    breakfastcost=people*250*y
else:
    pass
print("")

check=input("Would you like to change any information?(Yes/No) ")
if check=="Yes":
  ro=0
  while ro==0:    
    print("1. Name")
    print("2. Phone No.")
    print("3. Room Cost")
    print("4. Amenities Cost")
    print("5. Breakfast Cost")
    print("6. None")
    check2=input("What option number would you like to choose? ")
    if check2=="1":
        name=""
        name=input("Enter Your Full Name: ")
        L.pop(0)
        L.append(name)
        ex=input("Would you like to change anything else? (Yes/No) ")
        if ex=="Yes":
            check2=input("What option number would you like to choose? ")
            continue
        else:
            break
    if check2=="2":
        phone=str(input("Enter Your Phone Number: "))
        L.pop(1)
        L.append(phone)
        ex=input("Would you like to change anything else? (Yes/No) ")
        if ex=="Yes":
            check2=input("What option number would you like to choose? ")
            continue
        else:
            break
    if check2=="3":
        print("Please Choose a Room.")
        print("These Are the Available Room Options:")
        print("Option 1. Room A (1 bed) - Rs. 3000")
        print("Option 2. Room B (2 beds) - Rs. 4000")
        print("Option 3. Room C (3 beds) - Rs. 5000")
        print("Option 4. Room D (4 beds) - Rs. 6000")
        print("")

        x=int(input("Please Enter Your Desired Option Number: "))
        roomcost=0
        n=0
        var=0
        no1=0
        no2=0
        no3=0
        no4=0
        while var==0:
         if(x==1):
            n=0
            n=int(input("How Many Rooms Would You Like? "))
            y=int(input("How many nights? "))
            no1+=n
            ch1=3
            if no1>3:
                print("Not enough rooms available, please choose another")
                print("Number of rooms available:",ch1-(no1-n))
                no1=no1-n
                x=int(input("Please Enter Your Desired Option Number: "))
                continue
            else:
                print("After Opting for Room A, Your Final Room(s) Cost Comes to Rs.", roomcost+(3000*y*n))
                roomcost=roomcost+(3000*y*n)
                n=0
                hello=input("Would you like to choose more rooms?(Yes/No) ")
                if hello=="Yes":
                    x=int(input("Please Enter Your Desired Option Number: "))
                else:
                    var=1
         elif(x==2):
            n=0
            n=int(input("How Many Rooms Would You Like? "))
            y=int(input("How many nights? "))
            no2+=n
            ch2=3
            if no2>3:
                print("Not enough rooms available, please choose another")
                print("Number of rooms available:",ch2-(no2-n))
                no2=no2-n
                x=int(input("Please Enter Your Desired Option Number: "))
                continue
            else:
                print("After Opting for Room B, Your Final Room(s) Cost Comes to Rs.", roomcost+(4000*y*n))
                roomcost=roomcost+(4000*y*n)
                n=0
                hello=input("Would you like to choose more rooms?(Yes/No) ")
                if hello=="Yes":
                    x=int(input("Please Enter Your Desired Option Number: "))
                else:
                    var=1
         elif(x==3):
            n=0
            n=int(input("How Many Rooms Would You Like? "))
            y=int(input("How many nights? "))
            no3+=n
            ch3=3
            if no3>3:
                print("Not enough rooms available, please choose another")
                print("Number of rooms available:",ch3-(no3-n))
                no3=no3-n
                x=int(input("Please Enter Your Desired Option Number: "))
                continue
            else:
                print("After Opting for Room C, Your Final Room(s) Cost Comes to Rs.", roomcost+(5000*y*n))
                roomcost=roomcost+(5000*y*n)
                n=0
                hello=input("Would you like to choose more rooms?(Yes/No) ")
                if hello=="Yes":
                    x=int(input("Please Enter Your Desired Option Number: "))
                else:
                    var=1
         elif(x==4):
            n=0
            n=int(input("How Many Rooms Would You Like? "))
            y=int(input("How many nights? "))
            no4+=n
            ch4=3
            if no4>3:
                print("Not enough rooms available, please choose another")
                print("Number of rooms available:",ch4-(no4-n))
                no4=no4-n
                x=int(input("Please Enter Your Desired Option Number: "))
                continue
            else:
                print("After Opting for Room D, Your Final Room(s) Cost Comes to Rs.", roomcost+(6000*y*n))
                roomcost=roomcost+(6000*y*n)
                n=0
                hello=input("Would you like to choose more rooms?(Yes/No) ")
                if hello=="Yes":
                    x=int(input("Please Enter Your Desired Option Number: "))
                else:
                    var=1
         else:
            print("Please Choose Either Option 1, 2, 3 or 4")
         print("")
         ex=input("Would you like to change anything else? (Yes/No) ")
        if ex=="Yes":
            check2=input("What option number would you like to choose? ")
            continue
        else:
            break

    if check2=="4":
        number=0
        amenitiescost=0
        while number==0:
            print("Option 1. Spa - Rs. 500 Per Person")
            print("Option 2. Bowling - Rs. 80 Per Game")
            print("Option 3. Table Tennis - Rs. 60 Per Person for 30 mins")
            print("Option 4. Mini Golf Course - Rs. 80 Per Person")
            print("Option 5. Swimming Pool - Rs. 50 Per Person for 2 hours")
            print("Option 6. None")
            print("")
            x=int(input("Please Choose Your Desired Option Number: "))

            if(x==1):
                people=0
                people=int(input("How Many People in Total? "))
                print("After Opting for Spa, Your Spa Cost Comes to Rs.",500*people)
                amenitiescost+=500*people
                print("")
        
                ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
                if(ask=="Yes"):
                    number=0
                else:
                    number=1
                print("")

            elif(x==2):
                people=0
                people=int(input("How Many People in Total? "))
                n=0
                n=int(input("How Many Games Would You Like PER PERSON? "))
                print("After Opting for Bowling, Your Bowling Cost Comes to Rs.", 80*people*n)
                amenitiescost+=80*people*n
                print("")
        
                ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
                if(ask=="Yes"):
                    number=0
                else:
                    number=1
                print("")
        
            elif(x==3):
                people=0
                people=int(input("How many people for table tennis? "))
                n=0
                n=int(input("How Many Rounds of 30mins Would You Like PER PERSON? "))
                print("After Opting for Table Tennis, Your Table Tennis Cost Comes to Rs.", 60*people*n)
                amenitiescost+=60*people*n
                print("")

                ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
                if(ask=="Yes"):
                    number=0
                else:
                    number=1
                print("")
        
            elif(x==4):
                people=0
                people=int(input("How Many People in Total?"))
                print("After Opting for Mini Golf Course, Your Mini Golfing Cost Comes to Rs.", 80*people)
                amenitiescost+=80*people
                print("")
        
                ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
                if(ask=="Yes"):
                    number=0
                else:
                    number=1
                print("")

            elif(x==5):
                people=0
                people=int(input("How Many In Total? "))
                n=0
                n=int(input("How Many Rounds of 2 Hours would you like PER PERSON? "))
                print("After Opting for Swimming Pool, Your Swimming Pool Cost Comes to Rs.", 50*people*n)
                amenitiescost+=50*people*n
                print("")
        
                ask=input("Would You Like to Choose More Amenities?(Yes/No): ")
                if(ask=="Yes"):
                    number=0
                else:
                    number=1
                print("")

            elif(x==6):
                number=1
            else:
                print("Please Choose Either Option 1, 2, 3, 4, 5 or 6")
                print("")
        else:
            amenitiescost=0
        ex=input("Would you like to change anything else? (Yes/No) ")
        if ex=="Yes":
            check2=input("What option number would you like to choose? ")
            continue
        else:
            break
    if check2=="5":
        breakfastcost=0
        bf=input("Will You Be Having Breakfast by the Hotel for Rs. 250 PER DAY?(Yes/No) ")
        print("")
        if(bf=="Yes"):
            people=int(input("How Many People In Total? "))
            breakfastcost=people*250*y
        else:
            pass
        ex=input("Would you like to change anything else? (Yes/No) ")
        if ex=="Yes":
            check2=input("What option number would you like to choose? ")
            continue
        else:
            break
    if check2=="6":
        pass
    else:
        print("Please Choose Either Options 1, 2, 3, 4, 5 or 6")
    
print("")
print("Room Cost = Rs.", roomcost)
print("Amenities Cost = Rs.", amenitiescost)
print("Breakfast Cost = Rs.", breakfastcost)
total=roomcost+amenitiescost+breakfastcost
print("Your Total Bill Is Rs.", total)
print("")
L.append(total)

z=random.randint(1,1000)
r=str(z)
m=random.choice(string.ascii_letters)
v=m.upper()
g=random.choice(string.ascii_letters)
k=g.upper()
d=v+r+k
print("Please Pay at the Reception When Your Token Number Is Called. Your Token Number Is",d)
print("")
print("We Hope You Enjoy Your Stay at Hotel Marbella,",name,"!")

def pro4():
 f=open("hotelrecord.csv","a",newline="\n")
 while True:
    dt=csv.writer(f)
    dt.writerow([name,phone,checkin,checkout,roomcost,amenitiescost,breakfastcost,total])
    break
pro4()
