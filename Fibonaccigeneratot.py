num= int(input("Enter a  Fibonacci series number : "))
a=int(input("Enter a  1st starting  point :"))
b=int(input("Enter a 2nd starting  point :"))


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