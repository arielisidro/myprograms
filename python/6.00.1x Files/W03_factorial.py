def factorial(n):
    factorial=1
    while n>0:
        factorial*=n
        n-=1
    return factorial
    
def factorialRecursive(n):

    if n==1:
        return n

    return n*factorialRecursive(n-1)
                    
n=int(raw_input("Please enter an integer : "))
print str(n)+'!='+str(factorial(n))
print str(n)+'!='+str(factorialRecursive(n))