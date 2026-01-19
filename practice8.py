# def hye(name,surname,ending="thankyou"):
#     print("good morning " + name + surname)
#     print(ending)
# hye("kiki " , " jain")
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n* factorial(n-1)
n=int(input("enter  a number: "))
print(factorial(n))