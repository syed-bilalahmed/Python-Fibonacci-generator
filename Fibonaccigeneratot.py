num= int(input("Enter a  Fibonacci series number : "))

#starting number are 0 and 1
a=0
b=1

print( a)
print(b)
#initialize
i=1
#generate Fibonacci series
while i<num:
    c=a+b
    a=b
    b=c

   
    print(c)
    i+=1