def genPrimes():
    primes=[]
    x=0
    while True:
        x+=1
        print "x:",x,primes
        isPrime=True
        for p in primes:
            if (x % p)==0 and p<>1:
                isPrime=False
                break
        if isPrime:
            primes.append(x)
            next=x
            yield next
                            
    