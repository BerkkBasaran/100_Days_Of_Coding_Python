# dictinary --> {Key: Value}

# yazımına dikkat et!!
# başlarken empty dictinary kullan
programming_dictinary = {
    "Bug": "An error in a program that prevents the program...",
    "Funciton": "fonksiyon",
    "Loop": "döngü"
    }
print(programming_dictinary["Funciton"])

# adding item to dictionary
programming_dictinary["Eklenti"] = "ekledik bakalım bir şeyler" # --> eklerken mevcut ismini yazıp = sonrasında yeni veriyi yazıyorsun

#örnek
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
# Create an empty dictionary to collect the new values.
student_grades = {}
 
# Loop through each key in the student_scores dictionary
for student in student_scores:
 
    #Get the value (student score) by using the key each time.
    score = student_scores[student]
 
    #Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'


# nested list in dictinary
capital = {
    "France": ["paris", "Lille", "Dijon"]
    }

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1]) # --> print "D"

#nested list in list in dictinary :D
travel_log = {
    "France": {
        "total_visits" : 12,
        "cities_visited" : ["paris", "Lille", "Dijon"]
        }
    }
print(travel_log["France"]["cities_visited"][2])

# print("\n" * 100) # --> clearing screen

fruits = {"apple":2, "pear": 4, "orange":9}
print(max(fruits, key=fruits.get))