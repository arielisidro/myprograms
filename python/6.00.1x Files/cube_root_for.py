x=int(raw_input('Enter an integer: '))
ans=0
for ans in range(0,abs(x)):

    if ans**3 ==abs(x):
        break
if ans**3!=abs(x):
    print(str(x)+' is not a perfect cube')
else:
    if x<0:
        ans=-1*ans
    print('Cube root of '+str(x)+' is ' +str(ans))    