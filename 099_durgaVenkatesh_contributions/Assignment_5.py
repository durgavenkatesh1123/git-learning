# Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).


Student_details = {
    "Name1":"Venkatesh", 
    "Age1":24,
    "Weight1":54,
    "Height1":5.4,
    "Name2":"Rajesh",
    "Age2":25,
    "Weight2":48,
    "Height2":5.8,
    "Name3":"Mahesh",
    "Age3":28,
    "Weight3":68,
    "Height3":5.2
}
Length = len(Student_details)
print("The length of the dictionary is",Length)
print("Print Entire Dictionary")
print(Student_details)
print("Print each and every key value pair seperately")
for key in Student_details:
    print(key, Student_details[key])
print("Print only values (Don't print keys)")
for key in Student_details:
    print(Student_details[key])
print("Enter the key value for which you want the value")
Key_Number = (input("Enter the number "))
print(Student_details[Key_Number])

