n=16
factor_count=0
for i in range (2,n+1):
    if n%i==0:
        #means i is a factors of n 
        print(i, end = ' ')
        factor_count+=1
        if factor_count==3:
            break
else:
    print("Alas! this may be a prime number")