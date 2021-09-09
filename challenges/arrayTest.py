# How much is true?

firstTest = [True, False, False, True, False]
secondTest = [False, False, False, False]
thirdTest = []

def count(a):
    returnValue = 0
    for i in range(len(a)):
        if (a[i]):
            returnValue += 1

    return returnValue

# Test arrays
print(count(firstTest))
print(count(secondTest))
print(count(thirdTest))
