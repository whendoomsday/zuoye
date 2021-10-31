a = int(input("请输入a的数"))       
n = int(input("请输入n的数"))    
c=a
sum = 0           
for i in range(1,n+1):
    sum = sum + c     
    c = c * 10 + a    
print(sum)
