"""
#函数 ：判断一个数是否是回文素数
def is_prirme(num):
    for i in range(2, int(num / 2)):  # range 的范围必须是整数
        if num % i == 0:
            return False
    else:
        return True

def is_palin(num):
    num_t = num
    num_p = 0
    while num_t != 0:
        num_p = num_t % 10 + num_p * 10
        num_t = int(num_t / 10)
    if num == num_p:
        return True
    else:
        return False

while True:
    num = int(input ("num = "))
    if is_palin(num) and is_prirme(num):
        print("OK")
    else:
        print("NO")
    ch = input("Continue(y/n):")
    if ch == "n":
        break
"""
"""
x = 1
def fun():
    global x  # x 是全局变量
    x = 2
fun()
print(x)
"""
#功能：输出year年，month月的第一天是星期几
def is_leap_year(year):
    if year % 400 == 0 or year %100 != 0 and year % 4 == 0:
        return True
    else:
        return False

def num_of_days_in_month(year, month):
    if month in(1,3,5,7,8,10,12):
        return 31
    elif month in(4,6,9,11):
        return 30
    elif is_leap_year(year):
            return 29
    else:
            return 28

def total_num_of_days(year, month):
    days = 0
    for  y in range(1800,year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365
    for m in range(1, month):
        days += num_of_days_in_month(year, m)
    return days

def get_start_year(year,month):
    return (3 + total_num_of_days(year, month)) % 7

year = int(input("year ="))
month = int(input("month ="))
print(get_start_year(year, month))



