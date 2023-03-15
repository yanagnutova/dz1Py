n = int(input('Enter n:\n')) 

a = n % 10
b = n // 10 % 10
c = n // 100 % 10

d = n // 1000 % 10
e = n // 10000 % 10
f = n // 100000 % 10


bilet1 = a+b+c

bilet2 = d+e+f
if bilet1 == bilet2:
    print ("Yes", bilet1 + bilet2)
else: 
    print ("No, error!")