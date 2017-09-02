def caesar_cipher(stri, sh):
    ans = ""
    for i in stri:
        ans += chr((ord(i) + sh) % 256)
    return ans


print(caesar_cipher("abc", 1))
