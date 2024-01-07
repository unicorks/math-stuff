def calculate(n):
    nums = {}
    for i in range(1, n):
        lst = [n, -(i)]
        last = '-ve'
        while True:
            next = lst[-1] + lst[-2]
            if (next < 0 and last == '-ve') or (next > 0 and last == '+ve') or next == 0:
                break
            lst.append(next)
            last = '+ve' if next > 0 else '-ve'
        nums[i] = lst

    return nums

e = calculate(100)
for num, pattern in e.items():
    print(num, " : ", len(pattern), " : ", pattern)