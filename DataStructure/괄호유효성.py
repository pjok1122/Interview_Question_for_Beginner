'''
{([123456])} 과 같은 문자열이 들어왔을 때 유효성을 검사하자.
'''

left = ['{', '[', '(']
right = ['}', ']', ')']

string = input()


def is_valid(string):
    stack = []
    for s in string:
        if s in left:
            stack.append(s)
        elif s in right:
            check = stack.pop()
            if left.index(check) != right.index(s):
                return False

    if len(stack) > 0:
        return False
    else:
        return True


print(is_valid(string))
