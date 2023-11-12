def entry():
    name = input("enter your name here: ")
    entry = input("Entry ticket is 300$ [Yes][No]: ").lower()
    if entry != 'yes':
        print("Ok No Problem And Get Lost!")
    else:
        auction()

def auction():
    cars = 0
    items = [
        ["\n1. First car is an Ferrari 250 GTo",3000000],
        ["\n2.Second car is a very rare Ford Gt40",2000000],
        ["\n3. Third car is one and only  Bugatti La Voiture Noire",10000000],
        ["\n4. Fourth car is Aston Martin DBR1",1000000],
        ['\n5. Fifth car is Ferrari F40',5000000]
    ]
    
    for i in range(len(items)):
        print(items[i][0])


        for i in range(0,4):
            bid_amount = int(input("\nEnter your amount for bid$ (0 to quit): "))

            if bid_amount >= items[i][1]:
                print(f"Congrats you have own this car")
                cars += 1
                break

            elif bid_amount == 0:
                break       

            else:
                print("Your amount is too low for this car\n")
                print(f"You have try {i} attempts  to bid total 3 trys\n")

                if i == 3:
                    print("You have lost this car!")
                    break
                
    print(f"You have own total {cars} cars with today auction")

entry()