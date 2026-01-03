def summation(n):
    sum = 0

    for i in range(n + 1):
        sum += i

    return sum


def final_row(s, d, r, sum):
    row = []

    for i in range(r, 0, -1):
        row.append(s + (d * (sum - i)))

    for i in range(len(row)):
        row[i] = hex(row[i])

    return row


def final_row_sum(row):

    values = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    sum = 0

    for i in range(len(row)):
        row[i] = row[i][2:]
        for j in range(len(row[i])):
            sum += values[row[i][j]]
    
    while sum >= 16:
        sum = hex(sum)
        sum = sum[2:]
        digit_values = []
        for i in range(len(sum)):
            digit_values.append(values[sum[i]])
            
        sum = 0
        
        for i in range(len(digit_values)):
            sum += digit_values[i]

    sum = hex(sum)
    sum = sum[2:]

    return sum

sums = []

for i in range(5):
    s, d, r = input().split()
    s = int(s, 16)
    d = int(d, 16)
    r = int(r)

    row = final_row(s, d, r, summation(r))

    sums.append(final_row_sum(row))

for i in range(5):
    print(sums[i])