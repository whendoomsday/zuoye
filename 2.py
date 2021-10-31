'2'
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and a + c > b and b + c > a:
    d=a+b+c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    area=('%.4f'%area)
    if a*b or a*c or b*c ==2*area:
         print(d,area,"Ture")
    else:
         print(d,area,"False")
else:
    print('不能构成三角形')
