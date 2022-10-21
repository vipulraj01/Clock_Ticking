# Making a clock degree finder
print("Enter the hour and minute seperated by :  ")
hour,minute = map(int,input().split(":"))
a = 30*hour
b = 11/2*minute
formula = a-b
