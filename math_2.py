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

# calculate max length of alternating pattern and the number which gave it for a range of numbers
# so that i can try finding the relation between them

def calculate_more(start, end):
    numbers = {} # dict to store number, max alt integer, pattern
    for i in range(start, end + 1):
        e = calculate(i)
        lists = e.values()
        lists = sorted(lists, key=len, reverse=True)
        key = list(filter(lambda x: e[x] == lists[0], e))[0]
        numbers[i] = [key, lists[0]]
    return numbers

numbers = calculate_more(2, 100)
for k, v in numbers.items():
    print(k, " : ", v[0], " : ", len(v[1]), " : ", v[1])
        
