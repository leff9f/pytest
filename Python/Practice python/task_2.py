#list of all the divisors of that number

a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b=int(input('digit for check:\n'))
ddd=0
for i in a:
   if i%b==0:
       ddd+=1

print(ddd)
