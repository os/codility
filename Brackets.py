CHAR_MAP = {'(': ')', '{': '}', '[': ']'}


def solution(S):
    if not S:
        return 1

    if len(S) < 2:
        return 0

    stack = []
    for s in S:
        if s in CHAR_MAP:
            stack.append(s)
        else:
            if not stack:
                return 0

            c = stack.pop()
            if s != CHAR_MAP[c]:
                return 0

    return 1 if stack else 0
