from math import sqrt
import sys
num1 = int(sys.argv[1])
for i in range(2,int(sqrt(num1))+1):
    if(num1%i == 0):
        print(f"{num1} Is Not A Prime Number")
        break
else:
    print(f"{num1} Is A Prime Number")
