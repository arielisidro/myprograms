import string

def fillChars(chars):
    for i in string.ascii_lowercase:
        chars.append(i)

def getColumnNumber():
    columnNumber=int(raw_input("Please input cell number: "))
    return columnNumber

                                
def printColumns(chars):
    printBlank=True
    counter=1
    for c0 in chars:
        for c1 in chars:
            if printBlank:
                start2=0
                printBlank=False
            else:
                start2=1
            for c2 in chars[start2:]:
                print counter,':',
                for c3 in chars[1:]:
                    print c0+c1+c2+c3,
                    counter += 1
                print
            raw_input("pause for a while")
        
def printColumns2(columnNumber):
    counter=1
    aColumn=1
    while aColumn<=columnNumber:
        if aColumn % 26 ==1:
            print
            print counter,':',
        print getEquivalentColumn(computeColumnRecursive(aColumn,[])),
        counter+=1
        aColumn+=1

    
def computeColumn(columnNumber):
    base=26
    column=[]
    while columnNumber>0:
        col=columnNumber % base
        columnNumber/=base
        if col==0:
            col=base
            columnNumber=columnNumber-1
        column.insert(0,col)
            
    return column

def computeColumn(columnNumber,column):
    
    if columnNumber==0:
        return column
    print 'overloading'
    base=26
    col=columnNumber % base
    columnNumber/=base
    if col==0:
        col=base
        columnNumber=columnNumber-1

    column.insert(0,col)

    return computeColumn(columnNumber,column)

def computeColumnRecursive(columnNumber,column):
    
    if columnNumber==0:
        return column
    
    base=26
    col=columnNumber % base
    columnNumber/=base
    if col==0:
        col=base
        columnNumber=columnNumber-1

    column.insert(0,col)

    return computeColumnRecursive(columnNumber,column)


def getEquivalentColumn(column):
    columnLetter=''
    for i in column:
        columnLetter+=string.ascii_uppercase[i-1]
    return columnLetter


def printEquivalentColumn(column):
    for i in column:
        print string.ascii_uppercase[i-1],
            

if __name__ == '__main__':

    #chars=['',]
    #fillChars(chars)
    #printColumns2(getColumnNumber())
    
    printEquivalentColumn(computeColumn(getColumnNumber()))
    printEquivalentColumn(computeColumn(getColumnNumber(),[]))
