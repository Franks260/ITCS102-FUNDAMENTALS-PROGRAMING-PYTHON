

months = ['jan','feb','mar','apr','may']
months.append('jan')
print(months)
months.pop()
print(months)
months.append('jan')
print(months)

for i in months:
    print(f"{i}, 2023")
