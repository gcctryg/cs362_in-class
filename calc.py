def cal(a, b):
    summation = a + b
    print(summation)
    subtraction = a - b
    print(subtraction)
    multiplication = a * b
    print(multiplication)
    division = a / b
    print(division)

    myList = [summation, subtraction, multiplication, division]
    Sum = sum(myList)
    return Sum

print(cal(1,2))