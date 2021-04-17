def cal_divisor(x):
    i = 1
    while(i <= x):
        if(x % i == 0):
            print(i)
        i = i + 1

cal_divisor(100)