""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(values[0])
    print(values[6]) """

""" values = [1,2,5,7]

print(values)
for i in values:
    print(values[0])
 """
""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" 
sentence = input("Input a sentence") """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")
 """
""" def discount(age, isMember, isResident):
    if age <= 12 or age >=65:
        print("discount")

    elif isMember == True:
        print("discount")
    elif isResident == True:
        print("discount")
    else:
        print("no discount")
discount(30, False, False) """

""" x = "test"
print(f"hello {x}") """
""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" number = int(input("Input a number - "))
if int(number) % 2 == 0:
        print("even")
else:
        print("odd") """
""" 
service = input("Service? (bad, okay, good, or great?)")
bill = float(input("Bill value: "))
if service == "bad":
    print("0% tip")
elif service == "okay":
    print("15% tip")
elif service == "good":
    print("20% tip")
elif service == "great":
    print("25% tip") """

""" number = int(input("Enter number - "))
for i in range (1, int(number*0.5) +1,):
    if number % i == 0:
        print(i)
print(number) """


def gcf(number1,number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1

number1 = int(input("Enter number 1 - "))
number2 = int(input("Enter number 2 - "))

print("GCF:", gcf(number1,number2))


