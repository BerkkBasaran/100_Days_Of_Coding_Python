print("Welcome to the Python Pizza Delivery!")
size = input("What size pizza do you want? S, M, L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input("Do you want extra cheese? Y or N:\n") 
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25 
    if pepperoni == "Y":
        bill += 3
else:
    print("You typed wrong!")        
if extra_cheese == "Y":
    bill += 1

print(f"please pay ${bill}")


      