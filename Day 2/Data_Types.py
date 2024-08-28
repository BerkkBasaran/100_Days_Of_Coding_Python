
#Data types
#Strings - used with ""
# substring starts from 0

# ilk karakteri basma
print("Hello"[0])
# o yu basma 
print("Hello"[4])
# başlangıçtan şu indexe kadar , tersi de indeksten sona kadar
print("Hello"[:3])

#tersten sayar
print("Hello"[-1])

#string
print("123" + "456")

# Integer 
# - is used to see the number easily. it odes not affect
print(123 + 456)
print(123_456)

#Float is decimal point
print(3.145)

#Boolean = True / False

# len function does not accept int
len("12345")

# eadh function works with particular data type
# gives the type of variable
print(type("Hello"))
print(type(123))
print(type(1.23))
print(type(True))

# Type Conversion/Casting

#convert to int
int("123")

#print(int("123"+int("456")))
#Value errror

print("Number of letters in your name: " + str(len(input("Enter your name"))))


