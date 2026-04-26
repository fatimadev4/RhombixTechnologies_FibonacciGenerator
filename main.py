# # Fibonacci Generator 
# fibonacci series is a sequence  where each number is the sum of the two preceding numbers,
# defined by a mathematical recuurence relation.


# user -> gives input
# backend -> logic to create fibonacci series


user_input = int(input("Enter the number to see its fibonacci sequence series: "))

def fibonacci(user_input):
    a , b = 0 , 1
    for i in range(user_input):
        yield a  # yield : used inside the function to create a generator
        a , b = b , a + b

for num in fibonacci(user_input):
    print(num)
        
