import math
print ("Enter the coefficients for the given quadratic equation:")
print ("ax^2 + bx + c = 0")

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

discriminant = b**2 - 4*a*c
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant))/2*a
    x2 = (-b - math.sqrt(discriminant))/2*a
    print("x1= ",x1)
    print("x2= ",x2)
elif discriminant == 0:
    x = -(b/2*a)
    print("x= ",x)
else:
    print ("There are no roots!")