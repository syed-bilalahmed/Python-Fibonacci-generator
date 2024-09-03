num = int(input("Enter the number of terms in the Fibonacci series: "))
a = int(input("Enter the 1st starting point: "))
b = int(input("Enter the 2nd starting point: "))

# Print the first two starting points
print(a)
print(b)
# Starting from 2 because the first two terms are already printed
i = 0 
# Generate the Fibonacci series
while i < num:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1
