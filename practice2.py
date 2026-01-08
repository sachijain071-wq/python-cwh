# =int(input("Enter a number:"))
# for i in range(11):
#     print(f" {n} x {i}={n*i}")

n=int(input("enter a number: "))
for i in range(2,n): 
    if(n%i==0):
        print("it is not prime")
        break
