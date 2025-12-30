def Calculate(m,n):
    total=0
    for i in range(m, n + 1):
        if i % 15==0:
            total += i
            return total
#sample Inputs
m = int(input("Enter m: "))
n = int(input("Enter n: "))
result = Calculate(m, n)
print("sum =", result)
