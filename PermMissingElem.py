def solution(A):
    difference = 0
    length = len(A)
    for i in xrange(length):
        difference += i + 1 - A[i]

    difference += length + 1
    return difference
