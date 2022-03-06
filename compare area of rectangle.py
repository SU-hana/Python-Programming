""" CREATE A CLASS RECTANGLE WITH PRIVATE ATTRIBUTES LENGTH AND WIDTH. OVERLOAD ‘<’ 
OPERATOR TO COMPARE THE AREA OF 2 RECTANGLE. """

class rectangle():
    __length = None
    __width = None
    def __init__(self):
       self.__length = int(input("Enter the length: "))
       self.__width = int(input("Enter your width: "))
    def area(self):
       return(self.__length*self.__width)


r1 = rectangle()
r2 = rectangle()
print("Area of Rectangle = ", r1.area())
print("Area of Rectangle = ", r2.area())
if r1.area() < r2.area():
    print("Area 2 is greater")
else:
    print("Area 1 is greater")