# Convert age to days

myAge = 31
daysInYear = 365
totalDaysAlive = 0

count = 1
for year in range(myAge):
    if count <= myAge:
        totalDaysAlive += daysInYear
        count += 1
    
print('Age:', myAge, 'Days Alive:', totalDaysAlive)
