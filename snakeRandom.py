sides = int(input("How many sides on your dice? "))
while sides < 3:
    print("Sorry, that's not a valid size value. Please enter a size of at least 3.")
    sides = int(input("How many sides on your dice? "))
if sides >= 3:
    print("Thanks! Here we go...")
    
from random import seed
from random import randint
seed(1)
    
value = randint(1,sides)
value2 = randint(1,sides)

tracker = float(0.0)
val1A = float(0.0)
val2A = float(0.0)
average1 = float(0.00)
average2 = float(0.00)
double = 0

while value > 1 or value2 > 1:
    value = randint(1,sides)
    value2 = randint(1, sides)
    val1A = val1A + value
    val2A = val2A + value2
    tracker = tracker + 1
    if value == value2:
        double = double + 1
    
    print("die number 1 is %d and die number 2 is %d" % (value, value2))
    
    
if value == 1 and value2 == 1:
    print("You got snake eyes! Finally! On try number %d" %tracker)
    print("Along the way you rolled doubles {} times" .format(double))
    average1 = float(val1A) / tracker
    average2 = float(val2A) / tracker
    finalA1 = round(average1, 2)
    finalA2 = round(average2, 2)
    print("The average roll for die #1 was {}" .format(finalA1))
    print("The average roll for die #2 was {}" .format(finalA2))
