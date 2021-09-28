i = 1
u = 100

print("Prime numbers between", i, "and", u, "are:")

for num in range(i, u+ 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)