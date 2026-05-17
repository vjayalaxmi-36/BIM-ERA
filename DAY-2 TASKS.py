#DAY-2 TASKS
#________________

#1. Check employee promotion eligibility

age = int(input("enter a employee age:"))
exp = int(input("enter yrs of experience:"))
sal = int(input("enter a employee sal:"))
if age>25 and exp>5 and sal>50000:
    print("Eligible for Promotion")
else:
    print("Not Eligible")
#_____________________________________________________________________

#2. Check student distinction category

maths = int(input("enter marks for maths:"))
science = int(input("enter marks for science:"))
english = int(input("enter marks for english:"))
if maths>=75 and science>=75 and english>=75 :
    print("Distinction")
elif maths>=35 and science>=35 and english>=35 :
    print("Pass")
else:
    print("fail")
#_____________________________________________________________________

#3. Check website login system

username = input("Enter Username : ")
password = input("Enter Password : ")
otp = int(input("Enter OTP : "))
if username == "admin" and password == "1234" and otp == 5678:
 print("Login Successful")
else:
 print("Invalid Credentials")
#_____________________________________________________________________

#4. Check internet package category

speed = int(input("Enter Speed : "))
data = int(input("Enter Data Usage : "))
days = int(input("Enter Remaining Days : "))
if speed > 100 and data > 500 and days > 20:
 print("Premium Plan")
elif speed > 50 and data > 200:
 print("Standard Plan")
else:
 print("Basic Plan")
#____________________________________________________________________

#5. Check job eligibility

degree = input("Do You Have Degree : ")
experience = int(input("Enter Experience : "))
age = int(input("Enter Age : "))
if degree == "yes" and experience >= 2 and age > 21:
 print("Eligible for Interview")
else:
 print("Not Eligible")
#_____________________________________________________________________

#6. Check flight boarding eligibility

ticket = input("Ticket Available : ")
passport = input("Passport Available : ")
luggage = int(input("Enter Luggage Weight : "))
if ticket == "yes" and passport == "yes" and luggage < 30:
 print("Boarding Allowed")
else:
 print("Boarding Denied")
#_____________________________________________________________________

#7. Check scholarship eligibility

marks = int(input("Enter Marks : "))
attendance = int(input("Enter Attendance : "))
income = int(input("Enter Family Income : "))
if marks >= 85 and attendance >= 90 and income < 300000:
 print("Scholarship Approved")
else:
 print("Scholarship Rejected")
#_____________________________________________________________________

#8. Check mobile unlock system

pin = int(input("Enter PIN : "))
face = input("Face Detected : ")
fingerprint = input("Fingerprint Verified : ")
if pin == 1234 and face == "yes" and fingerprint == "yes":
 print("Mobile Unlocked")
else:
 print("Access Denied")
#_____________________________________________________________________

#9. Check hotel booking eligibility

pin = int(input("Enter PIN : "))
face = input("Face Detected : ")
fingerprint = input("Fingerprint Verified : ")
if pin == 1234 and face == "yes" and fingerprint == "yes":
 print("Mobile Unlocked")
else:
 print("Access Denied")
#______________________________________________________________________

#10. Check exam topper category

sub1 = int(input("Enter Subject 1 Marks : "))
sub2 = int(input("Enter Subject 2 Marks : "))
sub3 = int(input("Enter Subject 3 Marks : "))
total = sub1 + sub2 + sub3
if total >= 270:
 print("Topper")
elif total >= 180:
 print("Average")
else:
 print("Needs Improvement")
#______________________________________________________________________

#11. Check gym membership category

age = int(input("Enter Age : "))
weight = int(input("Enter Weight : "))
height = float(input("Enter Height : "))
if age > 18 and weight > 50 and height > 5.5:
 print("Fitness Category A")
elif age > 18 and weight > 40:
 print("Fitness Category B")
else:
 print("Basic Category")
#______________________________________________________________________

#12. Check traffic penalty system

helmet = input("Helmet Worn : ")
license = input("License Available : ")
speed = int(input("Enter Speed : "))
if helmet == "yes" and license == "yes" and speed < 80:
 print("No Fine")
elif speed > 100:
 print("Heavy Fine")
else:
 print("Normal Fine")
#______________________________________________________________________

#13.Check movie ticket pricing

age = int(input("Enter Age : "))
day = input("Enter Day : ")
member = input("Membership Available : ")
if age < 18 and member == "yes" and day == "Sunday":
 print("50% Discount")
elif member == "yes":
 print("25% Discount")
else:
 print("No Discount")
#______________________________________________________________________

#14. Check weather alert system

temperature = int(input("Enter Temperature : "))
wind = int(input("Enter Wind Speed : "))
rain = input("Is Raining : ")
if temperature > 40 and wind > 50 and rain == "no":
 print("Heat Alert")
elif rain == "yes" and wind > 60:
 print("Storm Alert")
else:
 print("Normal Weather")
#______________________________________________________________________

#15. Check online shopping offer

amount = int(input("Enter Purchase Amount : "))
coupon = input("Coupon Applied : ")
member = input("Premium Member : ")
if amount > 10000 and coupon == "yes" and member == "yes":
 print("Maximum Discount")
elif amount > 5000 and coupon == "yes":
 print("Medium Discount")
else:
 print("No Discount")
#______________________________________________________________________

#16. Check server room access

idcard = input("ID Card Available : ")
fingerprint = input("Fingerprint Verified : ")
accesslevel = int(input("Enter Access Level : "))
if idcard == "yes" and fingerprint == "yes" and accesslevel > 5:
 print("Access Granted")
else:
 print("Access Restricted")
#______________________________________________________________________

#17. Check sports team selection

speed = int(input("Enter Speed Score : "))
fitness = int(input("Enter Fitness Score : "))
discipline = int(input("Enter Discipline Score : "))
if speed > 80 and fitness > 80 and discipline > 80:
 print("Selected")
elif speed > 60 and fitness > 60:
 print("Waiting List")
else:
 print("Rejected")
#______________________________________________________________________

#18. Check laptop purchase recommendation

budget = int(input("Enter Budget : "))
ram = int(input("Enter RAM : "))
storage = int(input("Enter Storage : "))
if budget > 100000 and ram >= 16 and storage >= 512:
 print("Gaming Laptop")
elif budget > 50000 and ram >= 8:
 print("Office Laptop")
else:
 print("Basic Laptop")
#______________________________________________________________________

#19. Check bank loan approval

salary = int(input("Enter Salary : "))
creditscore = int(input("Enter Credit Score : "))
experience = int(input("Enter Experience : "))
if salary > 50000 and creditscore > 750 and experience > 3:
 print("Loan Approved")
elif salary > 30000 and creditscore > 650:
 print("Loan Under Review")
else:
 print("Loan Rejected")
#______________________________________________________________________

#20. Check smart home security system
door = input("Door Closed : ")
camera = input("Camera Active : ")
alarm = input("Alarm Enabled : ")
if door == "yes" and camera == "yes" and alarm == "yes":
 print("Home Secure")
else:
 print("Security Warning")