#DAY-1 TASKS
#________________

#1. Check whether employee age is above 21 and salary is above 30000

age = int(input("enter a employee age:"))
sal = int(input("enter a employee sal:"))
if age>21 and sal>30000:
    print("above")
else:
    print("below")
#_____________________________________________________________________

#2. Check whether student passed in two subjects

sub1 = int(input("enter marks for Subject1:"))
sub2 = int(input("enter marks for subject2:"))
if sub1>35 and sub2>35 :
    print("Pass")
else:
    print("fail")
#_____________________________________________________________________

#3. Check whether entered value is between two ranges

num = int(input("enter a number:"))
if num<10 and num>50:
    print("num is bw in range")
else:
    print("num is not bw in range ")
#_____________________________________________________________________

#4. Check whether username and password are correct

username = "vijju"
password = "3611"
un = input("enter username:")
pw = input("enter password:")
if un==username and pw == password:
    print("login successful")
else:
    print("login failed")
#____________________________________________________________________

#5. Check whether temperature is within safe range

temp = int(input("enter a temp:"))
if temp>20 and temp<30:
    print("safe temp")
else:
    print("unsafe temp")
#_____________________________________________________________________

#6. Check whether both entered numbers are even

n1 = int(input("enter a number1:"))
n2 = int(input("enter a number2:"))
if n1%2==0 and n2%2==0:
    print("Even")
else:
    print("Odd")
#_____________________________________________________________________

#7. Check whether both entered numbers are positive

n1 = int(input("enter a number1:"))
n2 = int(input("enter a number2:"))
if n1>0 and n2>0:
    print("Positive")
else:
    print("negative")
#_____________________________________________________________________

#8. Check whether person is eligible for driving

age = int(input("enter age:"))
lic = input("do u have licence(yes/no)")
if age>=18 and lic=="yes":
    print("eligible")
else:
    print("not eligible")
#_____________________________________________________________________

#9. Check whether project progress meets deadline condition

days = int(input("Enter remaining days: "))
progress = int(input("Enter project progress : "))
if days > 5 and progress >= 80:
    print("deadline condition")
else:
    print("not deadline condition")
#______________________________________________________________________

#10. Check whether attendance and marks satisfy eligibility

attendance = int(input("Enter attendance per: "))
marks = int(input("Enter marks: "))

if attendance >= 75 and marks >= 35:
    print("Eligible")
else:
    print("Not eligible")
#______________________________________________________________________

#11. Check whether entered role is Admin or Manager

role = input("Enter role: ")
if role == "Admin" or role == "Manager":
    print("Access granted")
else:
    print("Access denied")
#______________________________________________________________________

#12. Check whether student scored distinction in any one subject

sub1 = int(input("Enter subject1 marks: "))
sub2 = int(input("Enter subject2 marks: "))
if sub1 > 75 or sub2 > 75:
    print("Student got distinction")
else:
    print("No distinction")
#______________________________________________________________________

#13. Check whether entered day is weekend

day = input("Enter day: ")
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Not weekend")
#______________________________________________________________________

#14. Check whether selected category matches two possible values

category = input("Enter category: ")
if category == "Gold" or category == "Silver":
    print("Category matched")
else:
    print("Category not matched")
#______________________________________________________________________

#15. Check whether salary or experience satisfies requirement

salary = int(input("Enter salary: "))
experience = int(input("Enter experience in years: "))
if salary > 30000 or experience >= 5:
 print("Requirement satisfied")
else:
 print("Requirement not satisfied")
#______________________________________________________________________

#16. Check whether temperature is extremely low or high

temp = int(input("Enter temperature: "))
if temp < 10 or temp > 40:
    print("Temperature is extreme")
else:
    print("Temperature is normal")
#______________________________________________________________________

#17. Check whether entered username matches predefined values

username = input("Enter username: ")
if username == "admin" or username == "manager":
    print("Valid username")
else:
    print("Invalid username")
#______________________________________________________________________

#18. Check whether selected option belongs to given choices

option = input("Enter option(A/B/C): ")
if option == "A" or option == "B" or option == "C":
    print("Option matched")
else:
    print("Invalid option")
#______________________________________________________________________

#19. Check whether entered city matches allowed cities

city = input("Enter city: ")
if city == "Hyderabad" or city == "Chennai":
    print("City allowed")
else:
    print("City not allowed")
#_______________________________________________________________________

#20. Check whether entered number matches predefined values

num = int(input("Enter number: "))
if num == 10 or num == 20 or num == 30:
    print("Number matched")
else:
    print("Number not matched")
#_______________________________________________________________________

#21. Check Whether user is not admin

user = input("Enter username: ")
if not (user == "admin"):
    print("User is not admin")
else:
    print("User is admin")
#________________________________________________________________________

#22. Check whether entered number is not positive

number = int(input("Enter a number: "))
if not (number > 0):
    print("Number is not positive")
else:
    print("Number is positive")
#________________________________________________________________________

#23. Check whether entered value is not empty

value = input("Enter a value: ")
if not (value == ""):
    print("Value is not empty")
else:
    print("Value is empty")
#_________________________________________________________________________

#24. Check whether file is not available

file_avai = False
if not file_avai:
    print("File is not available")
else:
    print("File is available")
#_________________________________________________________________________

#25. Check whether employee is not active

active = False
if not active:
    print("Employee is not active")
else:
    print("Employee is active")
#_________________________________________________________________________

#26. Check whether project status is not correct

status = input("Enter project status: ")
if not (status == "completed"):
    print("Project is not completed")
else:
    print("Project is completed")
#_________________________________________________________________________

#27. Check whether password is not correct

password = input("Enter password: ")
if password != "admin123":
    print("Password is not correct")
else:
    print("Password is correct")
#_________________________________________________________________________

#28. Check whether temperature is not safe

temperature = int(input("Enter temperature: "))
if not (temperature >= 20 and temperature <= 30):
    print("Temperature is not safe")
else:
    print("Temperature is safe")
#__________________________________________________________________________

#29. Check whether selected option is not allowed

option = input("Enter option: ")
if not (option == "A"):
    print("Selected option is not allowed")
else:
    print("Selected option is allowed")
#___________________________________________________________________________

#30. Check whether marks are not passing marks

marks = int(input("Enter marks: "))
if not (marks >= 35):
    print("Marks are not passing marks")
else:
    print("Marks are passing marks")