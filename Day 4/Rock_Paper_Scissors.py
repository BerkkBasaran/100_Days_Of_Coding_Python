#random number --> 1st_part.2nd_part --> 1st_part = module , 2nd_part = function
    # random.random() --> 0.0 <= X < 1.0   
    # random.uniform(a,b) --> a <= N <= b (floating number)
    # docs.python.org/3/library/random.html check this site !!!

# random_heads_or_tails = random.randint(a:0, b:1)
# if andom_heads_or_tails == 0:
    #print("Heads")
# else:
#   #print("Tails")

#Lists --> rather than write seperate line of code, create list 
# fruits = ["apple", "pears", "banana", "pineapple"]
# list order --> print(fruits[2]) --> prints out "banana" --> list index starts from "0". " - index starts from end"
# list item change --> fruits[1] = "watermelon" , new list --> fruits = ["apple", "watermelon", "banana", "pineapple"] 
# for list extend or other actions --> google it

import random
# import my_module
choice_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
choice_pc = random.randint(0, 2)

if choice_user == 0:
    print('''     
        _______
    ---'   ____)
          (_____)
           (_____)
           (____)
    ---.__(___)   ''')
elif choice_user == 1:
    print('''    
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)     ''')
else:
    print('''     
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)    ''')
print("Computer chose: \n")

if choice_pc == 0:
    print('''     
        _______
    ---'   ____)
          (_____)
           (_____)
           (____)
    ---.__(___)   ''')
elif choice_pc == 1:
    print('''    
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)     ''')
else:
    print('''     
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)    ''')

if choice_pc == choice_user:
    print("Draw")
elif choice_pc == 0 and choice_user == 1:
    print("You win!")
elif choice_pc == 1 and choice_user == 2:
    print("You win!")
elif choice_pc == 2 and choice_user == 0:
    print("You win!")
else:
    print("You lose! Try again.")

# later try to solve this example with creating list !!!