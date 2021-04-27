myAge = 31
daysInYear = 365
totalDaysAlive = 0

count = 1
for year in range(31):
    if count <= myAge:
        totalDaysAlive += daysInYear
        count += 1
    
print('Age:', myAge, 'Days Alive:', totalDaysAlive)
