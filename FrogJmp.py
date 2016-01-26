def solution(X, Y, D):
    distance = Y - X
    if not distance:
        return 0

    remainder = distance % D
    jumps = distance / D
    if remainder:
        jumps += 1

    return jumps
