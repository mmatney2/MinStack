def isValid(str):
    stack = []
    closeToOpen = {')': '(', ']':'[', '}':'{'}

    for s in str:
        print(s)
        if s in closeToOpen: #if s is a key:
            if stack and stack[-1] == closeToOpen[s]: #if list has value of open parenthesis
                print(closeToOpen[s])
                stack.pop()
            else:
                return False
        else:
            stack.append(s)
    return True if not stack else False
print(isValid('([])'))