
d= int(input("Enter the number of days\n "))\
   *3600 * 24
h= int(input("Enter the number of hours\n "))\
   * 3600
m= int(input("Enter the number of minutes\n "))\
   * 60
s= int(input("Enter the number of seconds\n "))

t= d + h  + m + s

print("Number of seconds is ", t)
