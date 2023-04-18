Normal_seat=1500
VIP_seat=500
import datetime
while True:
    n=input("Enter name:" )
    print("")
    total=0
    while True:
        current_time = datetime.datetime.now()
        print(current_time)
        print("""WELCOME TO STADIUM!!
        Press 1 for Normal seat
        Press 2 for VIP seat""")
        x=int(input("Enter preference:" ))
        if x==1:
            if Normal_seat>0:
                print("You have opted for Normal seat")
                a = int(input("How many seats do you want?"))
                if a>Normal_seat:
                    print("We only have", Normal_seat, "seats")
                else:
                    total += (a * 200)
                    Normal_seat -= a
            else:
                print("Sorry! We are house-full")
        elif x==2:
            if VIP_seat>0:
                print("You have opted for VIP seat")
                b = int(input("How many seats do you want?" ))
                if b>VIP_seat:
                    print("We only have", VIP_seat, "seats")
                else:
                    total += (b * 500)
                    VIP_seat -= b
            else:
                print("Sorry! We are house-full")
        else:
            print("Invalid Input")
        print("""Press 1 for snacks
        Press 2 for bill 
        Press 3 for seat choice""")
        s=input("Enter preference:"  )
        if s=="1":
            total += 100
            print(total)
            break
        elif s=="2":
            print(total)
            break
        elif s=="3":
            continue
