# creating function for repeating codes could be benefial
# def my_function() --> normal hali
# def my_function(something) --> add variable to function
#   do this with something
#   do that by something


# function with one input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

# something = 123 --> parameter = Arguement
greet_with_name("Angela")

# function with more than one input
def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# something = 123 --> parameter = Arguement
greet_with_name("Angela", "Nowhere") #order matters
greet_with_name("Nowhere", "Angela") #order matters --> wrong order
greet_with_name(location = "Nowhere", name = "Angela") # writing with parameter helps to solve order problem

# true love calculation example
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")