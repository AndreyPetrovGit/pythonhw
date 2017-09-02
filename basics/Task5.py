def histogram(arr):
    res = ""
    for i in arr:
        for j in range(0, i):
            res += "*"
        res += "\n"
    return res
print(histogram([1,2,3]))