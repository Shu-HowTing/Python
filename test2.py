#求解一元二次方程的解
import math
ch = ""
while(ch != "y"):
    a=float(input("input a:"))
    b=float(input("input b:"))
    c=float(input("input c:"))
    if a != 0:
        delta=b**2-4*a*c
        if delta<0:
            print("no solution!")
        elif delta==0:
            print("x=",-b/2*a)
        else:
            root=math.sqrt(b**2-4*a*c)
            x_1=(-b+root)/2*a
            x_2=(-b-root)/2*a
            print("x_1= ",x_1,"\n","x_2=",x_2)
    ch = input ("Quit?(y/n):")

