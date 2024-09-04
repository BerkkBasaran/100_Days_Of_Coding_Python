# functions with outputs
# .title() --> Başlık formatına getiriyor. first case upper rest lower
#return is the end of function, whatever you wrote, did not read

#return function
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("AnGeLa", "YU"))

# multiple return

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your name?"),input("What is your last name?")))

# örnek : leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# docstring --> fonksiyon yaratırken definition ın hemen altında ilk indent e yazılır.
# comment kısayolu --> (command + shift + 7 ) or (command / ) for mac     --> ctrl + / for windows
def format_name(f_name, l_name):
    """ Take a first and last name and format it to return the title case version of the name"""  # docstring örneği
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# örnek
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result) # result = 15

# örnek
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25)) # result --> None --> due to empty return function


