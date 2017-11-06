"""
def fun(a, b):
    return a+b
c=fun(1,2)
print(c)
print(type('小明'))
import math
print(math.sin(math.pi/2))
print(2**2**3)


print(123 and 456)

x=int(input('x:'))  #input 输入默认为str ，如果不加int，则输入的数字会被当成字符处理，而2*x即字符写两遍
print(2*x)


a=12
print(2*a)

print("the area is : ", a)  #此语句等价于print("the area is:%d" % a)
print("hello  \n world")
"""
x=61
gender="man"
if x>=60:
    if gender =="lady":
        print(x)
    else:
        print("no")
if x>=90:
    print('A')
else:
    if x>=80:
        print('B')
    else:
        if x>=70:
            print('C')
        else:
            if x>=60:
                print('D')
            else:
                print('E')


k=1
while k<=10:
    print(k)    #python严格遵守缩进的原则
    k+=1        #k+=1必须和print对齐，否则报错

