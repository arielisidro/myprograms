def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
        print e
    except ZeroDivisionError, e:
        print "x"
        print e        
    else:
        print "1"
    finally:
        print "ariel"