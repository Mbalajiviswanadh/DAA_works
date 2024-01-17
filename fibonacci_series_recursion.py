def fibonacci(n, calls_counter=None):
    if calls_counter is None:
        calls_counter = {'count': 0} 

    calls_counter['count'] += 1  

    if n <= 1:
        return n
    else:
        return fibonacci(n-1, calls_counter) + fibonacci(n-2, calls_counter)

# Take user input for the value of n
n = int(input("Enter the value of n: "))

# # Test the function for taken value of n
for n in range(n):
    calls_counter = {'count': 0}
    result = fibonacci(n, calls_counter)
    print(f"F({n}): {result}, Function calls: {calls_counter['count']}")

# Initialize calls_counter for the initial function call
calls_counter = {'count': 0}

# Call the fibonacci function with user input
result = fibonacci(n, calls_counter)

# Print the result and the number of function calls
print(f"-------------------The function call for given:'{n}' value= -------------------")
print(f"F({n}): {result}, Function calls: {calls_counter['count']}")
