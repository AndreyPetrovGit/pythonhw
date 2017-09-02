def rev(str):
    ans = ""
    for ch in range( 0, len(str)):
        ans += str[len(str) -1 -ch]
    return ans
print(rev("Hello!"))

