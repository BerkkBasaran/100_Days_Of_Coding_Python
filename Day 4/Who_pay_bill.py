import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#lenght_of_list = len(friends)
random_number = random.randint(0,(len(friends)-1))  #len starts counting from 1,2,3,4 not zero.

print(friends[random_number])

#alternative way
#print(random.choice(friends))


# if you want to combine different lists --> dirty_dozen = [fruits, vegetables]


