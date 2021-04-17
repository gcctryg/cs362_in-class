import string
import random

print('Enter a number to generate a password: ')
x = input()
x = int(x)

res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = x))
  
print("The password is: " + str(res))
