def isPol(str):
    ans = True
    for ch in range( 0, len(str)//2):
        if str[ch] != str[len(str) - ch -1]:
            ans = False
            break
    return ans
print(isPol("1235321"))