s1 = "(()())"
s2 = "((())"

def balance(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if(len(stack) == 0):
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

def expr(s):
    opers = []
    lits = []
    for i in s:
        if i in "+-*/":
            opers.append(i)
        elif i != " ":
            lits.append(i)
print(balance(s2))
