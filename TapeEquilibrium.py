def solution(A):
    N = len(A)
    left_sum = A[0]
    right_sum = sum(A[1:])

    def get_difference():
        return abs(left_sum - right_sum)

    minimum = get_difference()

    for P in xrange(1, N - 1):
        left_sum += A[P]
        right_sum -= A[P]
        difference = get_difference()
        if difference < minimum:
            minimum = difference

    return minimum
