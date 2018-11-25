print("Q6")
import math
print("FIRST EQUATION OF MOTION")
vi = int(input("Enter the initial velocity :"))
a = int(input("Enter the acceleration :"))
t = int(input("Enter the time :"))
def lawsofmotion (vi,a,t):
    print("The initial velocity is:" , vi)
    print("The acceleration is:" , a)
    print("The time is:" , t)
    vf = vi + a*t
    print("The  final velocity is:" , vf)
lawsofmotion(vi,a,t)

print("SECOND EQUATION OF MOTION")
vi = int(input("Enter the initial velocity :"))
t = int(input("Enter the time :"))
a = int(input("Enter the acceleration :"))
def lawsofmotion(vi,t,a):
    print("The initial velocity is:" , vi)
    print("The time is:" , t)
    print("The acceleration is:" , a)
    s = (vi)*t + (1/2)*a*(t**2)
    print("The distance is :" , s)
lawsofmotion(vi,t,a)

print("THIRD EQUATION OF MOTION")
vi = int(input("Enter the initial velocity :"))
a = int(input("Enter the acceleration :"))
s = int(input("Enter the distance :"))
def lawsofmotion(vi,a,s):
     print("The initial velocity is:" , vi)
     print("The acceleration is:" , a)
     print("The distance is :" , s)
     vf = math.sqrt(vi + a*t)
     print("The final velocity is :" , vf**2)
lawsofmotion(vi,a,s)
     
     
     
    

    
    







