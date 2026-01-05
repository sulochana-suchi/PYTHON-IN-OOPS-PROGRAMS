days_map = {'mon':0, 'tue':1, 'wed':2, 'thu':3, 'fri':4, 'sat':5, 'sun':6}
start_day = input().strip().lower()
n = int(input())
# Find the day index of first sunday
first_sunday_in_days = (6 - days_map[start_day]) + 1
#  +1 because first dauy counts as day 1
if first_sunday_in_days > n:
    sundays = 0
else:
    remaining_days = n - first_sunday_in_days
    sundays = 1 + (remaining_days // 7)
print(sundays)
