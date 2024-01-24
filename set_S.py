# function to help in reducing fraction to lowest form
def GCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)


s = [[1, 1]]
while len(s) < 1000:  # sets an ending condition, can change the value after < to vary length of s
    # fulfills the b/2a condition 
    while True:
        last_num = s[-1]
        to_append = [last_num[1], 2*(last_num[0])]    # finds b/2a
        gcd = GCD(to_append[0], to_append[1])    # reduces the fraction
        to_append_1 = [to_append[0]//gcd, to_append[1]//gcd]
        if to_append_1 in s:   # breaks out of loop if new numbers can't be found using this
            break
        else:
            s.append(to_append_1)    # appends if the number is not yet in the set

    # fulfills the a+c/b+d condition
    # by running that on every number in s with every other number
    e = len(s)
    for i in range(0, e):
        for j in range(0, e):
            a, b = s[i][0], s[i][1]   # finds a/b
            c, d = s[j][0], s[j][1]   # finds c/d
            to_append = [a+c, b+d]
            gcd = GCD(to_append[0], to_append[1])    # reduces the fraction
            to_append_1 = [to_append[0]//gcd, to_append[1]//gcd]
            if to_append_1 not in s:
                s.append(to_append_1)    # appends if the number is not yet in the set

sorted_s = sorted(s, key= lambda x: x[0]/x[1])
decimal_s = list(map(lambda x: x[0]/x[1], s))
sorted_ds = sorted(decimal_s)
print(sorted_ds)
print(sorted_s)