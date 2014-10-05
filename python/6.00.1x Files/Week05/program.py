def program1(x):
    
    for i in range(1000):
        print i,
    print
    step=0
    total = 0
    step+=1
    for i in range(1000):
        total += i
        step+=1

    while x > 0:
        x -= 1
        step+=1
        total += x
        step+=1
    step+=1
    print step

    return total