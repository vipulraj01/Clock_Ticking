# Making a clock degree finder
print("Enter the hour and minute seperated by :  ")
hour,minute = map(int,input().split(":"))
a = 30*hour
b = 11/2*minute
formula = a-b
if formula>=180:
    z = int(abs(formula-360))
    if z>=180:
        z = int(abs(z-360))
    print(z,"°",sep="")
else:
    y = int(abs(formula))
    print(y,"°",sep="")
