cases = int(input())
for c in range(cases):
    n,b = list(map(int, input().split()))
    houses_values = list(map(int, input().split()))
    houses_values.sort()
    count = 0
    summation = 0
    for house in houses_values:
        if summation + house <= b:
            summation += house
            count += 1
        else:
            break
    print('Case #{}: {}'.format(c+1, count))
