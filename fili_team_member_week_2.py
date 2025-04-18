# store a data for 10 students using dictionary.
students = {
    'Ahmet Yilmaz': [85, 90, 78],
    'Mehmet Demir': [92, 88, 76],
    'Ayse Kaya': [78, 89, 95],
    'Zeynep Celik': [65, 70, 80],
    'Ali Kara': [50, 60, 55],
    'Fatma Yildiz': [88, 85, 90],
    'Murat Aydin': [72, 68, 74],
    'Elif Aksoy': [95, 90, 88],
    'Hakan Öztürk': [45, 50, 55],
    'Canan Taş': [80, 75, 82]
}

# 1- Calculating each student's GPA and add it to the dictionary.
for name, grades in students.items(): #loop through each student in the students dic.
    midterm, final, oral = grades
    GPA = (midterm * 0.3) + (final * 0.5) + (oral * 0.2) #calculate the GPA using the given formula
    students[name].append(GPA) #To add the caculated GPA to the end of the list of grades

# 2-To find the student with the highest GPA and print it on the screen
highest_gpa = 0
best_student = ""
for name, data in students.items():
    if data[3] > highest_gpa:
        highest_gpa = data[3] #data[3] GPA that just added(the 4th element)
        best_student = name
print(f"Highest GPA: {best_student} ({highest_gpa:.2f})")

# 3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.
names_list = [(name.split()[0], name.split()[1]) for name in students] #we use list comprehension

# 4-Sort the names in alphabetical order and print the sorted list on the screen.

sorted_names = sorted(names_list) #we use built-in fun
print("Sorted Names:", sorted_names)

# 5-Keep students with a GPA below 70 in a cluster (set).
below = {name for name, data in students.items() if data[3] < 70}
# we use a set comprehension 
print("Below 70 GPA:", below)
#if it is,we add the student's full name to the below set and finally print the below set.

