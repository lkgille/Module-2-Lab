"""
Lillian Gillenwater
File Name: GillenwaterModule2Lab.py
Desc: This app will accept a student's name and gpa,
then output whether they made the dean's list, honor roll,
or neither.

variables:
lastName - student's last name
firstName - student's first name
gpa - student's gpa

"""
while True:
    lastName = input("Enter the student's last name or 'ZZZ' to quit: ")

# while True:
    if lastName == "ZZZ":
        break
    else:
        firstName = input("Enter the student's first name: ")

    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(firstName + " " + lastName + " " + "made the Dean's List.")
    elif gpa >= 3.25:
        print(firstName + " " + lastName + " " + "made the Honor Roll.")
    else:
        print(firstName + " " + lastName + " " + "did not make the Dean's List or the Honor Roll.")