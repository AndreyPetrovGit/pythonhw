def isBalanced(string):
    open = 0
    close = 0
    for i in string:
        if i == "]":
            close += 1
        elif i == "[":
            open += 1
        if (close > open):
            return False
    if(open != close):
        return False
    return True
print(isBalanced("[[]]"))
print(isBalanced("[[]]]"))
print(isBalanced("[[[]]"))

print(isBalanced("]]]]]"))
print(isBalanced("[[[[["))
print(isBalanced(""))