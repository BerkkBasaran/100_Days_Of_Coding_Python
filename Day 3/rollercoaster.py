#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm?\n"))

#if height >= 120:
#    print("You can ride the rollercoaster.")
#    age = int(input("How old are you?\n"))
#    if age < 12:
#        print("Please pay $5")
#    else: #elif age < 18: olarak da kullanılabilir.
#        if age < 18:
#            print("Please pay $7")
#        else:
#            print("Please pay $12")
#else:
#    print("Sorry you have to grow taller before you can ride.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0 

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    if age < 12:
        print("Child tickets are $5")
        bill = bill + 5
    elif age < 18:
        print("Youth tickets are $7")
        bill = bill + 7
    elif age >= 45 and age <= 55:   
        print("Everything is going to be OK. Have a free ride on us!") 
    else:
        print("Adult tickets are $12")
        bill = bill + 12

    wants_photo = input("Do you want to have photo take? Type y for Yes and n for No.\n")
    if wants_photo == "y":
        bill += 3
        print(f"Please pay ${bill}")
    else:
        print(f"Please pay ${bill}")
        
else:
    print("Sorry you have to grow taller before you can ride.")    