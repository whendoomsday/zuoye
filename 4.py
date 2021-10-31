'4'
m=eval(input())
if m==2:
    print('Ture')
else:
    for i in range(2,m):
        if m%i==0:
            break
        if i==m-1:
            print('Ture')
        else:
            print('False')
