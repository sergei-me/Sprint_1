def digit_root(num):
    sum = 0
    s_num = str(num)
    for l in s_num:
        sum += int(l)
    if sum >= 10:
        digit_root(sum)
    else:
        return sum
    
print(digit_root(3453))