#a number classifier
numb = int(input("Enter the number"))
if numb > 0:
    print("Number is positive")
elif numb < 0:
    print("Number is negative")
else:
    print("Numbr is zero")

if numb % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#Grade calculator
score = int(input("enter score"))
if score >= 90:
    print("A grade")
elif score >= 70:
    print("B grade")
elif score >= 60:
    print("C grade")
elif score >=40:
    print("D grade")
else:
    print("F grade")

#password
password = "siva123"
input_password = input("Enter password here: ")
if password == input_password:
    print("login successfully")
else:
    print("incorrect password")

#Largest number
x = int(input("Enter a number"))
y = int(input("Enter a number"))
z = int(input("Enter a number"))
if x >= y and x >=z:
    print(x,"is largest number")
elif y >=x and y >= z:
    print(y,"is largest number")
else:
    print(z,"is the largest number")


