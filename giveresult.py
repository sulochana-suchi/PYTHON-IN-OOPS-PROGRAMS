def giveResult(s1, s2, s3):
    if s1 < s2:
        return "Good"
    elif s1 >= s2 and s1 <= s3:
        return "Best"
    else:
        return "can do better"
s1 = int(input("Enter s1: "))
s2 = int(input("Enter s2: "))
s3 = int(input("Enter s3: "))
print(giveResult(s1, s2, s3))
