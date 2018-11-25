print("Q7")

print("FOR HORIZONTAL RANGE")
Vx = int(input("Enter the horizontal velocity :"))
x = int(input("Enter the horizontal distance :"))
t = int(input("Enter time :"))
def HorizontalRange(Vx,x,t):
    print("The horizontal velocity is :", Vx)
    print("The horizontal distance is :", x)
    print("Time is :", t)
    x = Vx *(x)* t
HorizontalRange(Vx,x,t)

print("FOR VERTICAL RANGE")
g = int(input("Enter the gravitational acceleration :"))
t = int(input("Enter time :"))
def VerticalRange(g,t):
    print("The gravitational acceleration is :", g)
    print("Time is :", t)
    y = 1/2*(g)*(t**2)
VerticalRange(g,t)
    

