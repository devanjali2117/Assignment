n=12
count=2
while count < n: #count=2,3,4,5,6
    if n%count==0:
        #number n is perfectly divisible by count so it cannot be a prime number 
        print(n, "is not a prime number")
        break
    count+=1
else:
    print(n, "is a prime number")
