def sum(a):
    res = 0
    for ind in a:
        res = res + ind
    return res

print(sum([1,2,3]))

def mul(a):
    res = 1
    for ind in a:
        res *= ind
    return res
print(mul([12,3,4]))
