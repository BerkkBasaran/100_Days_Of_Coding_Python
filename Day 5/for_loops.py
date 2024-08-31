# for loops
fruits =  ["Apple" , "Peach", "Pear"]

for fruit in fruits:
    print(fruit)   # this loop prints out all the items in the list
    print(fruit + " pie") # üstteki koddan dolayı önce meyveyi sonra pie lı halini basacak. apple , apple pie , peach, peach pie  


student_scores = [150, 142 ,185, 120, 171, 184, 149, 24, 199]

total_exam_score = sum(student_scores)
max_number = 0

sum = 0
for i in student_scores:
    if i > max_number:
        max_number = i
    else:
        continue
print(max_number)  

#for loop with range function
# for number in range(1, 10) 1 er artacak
# for number in range(1, 10, 2) 2 şer artacak
total = 0
for number in range(1, 101):
    total += number
print(total)