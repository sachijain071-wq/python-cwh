# for i in range(1,20):
#     if i % 3 ==0 :
#         print("Fizz")
#     elif i % 5==0:
#         print("Buzz")
#     elif i % 3 ==0 and i % 5==0:
#         print("FizzBuzz")
#     else:
#         print(i)

def count_even(numbers):
    count = 0
    for num in numbers:
        if num %2 == 0:
            count += 1
    return count 
    
print(count_even([1,2,3,4,5,8]))
