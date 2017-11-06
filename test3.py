# if 语句

points = float(input("The leading scores:"))
has_ball = input("The leading team has ball(yes/no):")
rest_time = int(input("The rest seconds:"))
points-=3
if has_ball=="yes":
    points+=0.5
else:
    points-=0.5
if points<0:
    points=0
points **=2
if points>rest_time:
    print("safe")
else:
    print("not safe")


