distance = int(input("Enter distance:"))
horse1, horse2, horse3 = map(int, input("Enter speeds of 3 horses:").split())
fastest_speed = max(horse1, horse2,horse3)
time = distance // fastest_speed
print(time)
