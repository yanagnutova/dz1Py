n = int(input('Enter n:\n')) 
m = int(input('Enter m:\n')) 
k = int(input('Enter k:\n3')) 

if (k % n == 0 or k % m == 0) and k <= m*n:
    print ("yes")
else:
    print ("no") 