# def hye(name,surname,ending="thankyou"):
#     print("good morning " + name + surname)
#     print(ending)
# hye("kiki " , " jain")
def sum(n):
    if(n==0):
        return 0
    return  sum(n-1) + n
n=int(input("enter  a number: "))
print(sum(n))