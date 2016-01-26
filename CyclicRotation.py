def solution(A, K):
    if not A:
        return A

    if not K:
        return A

    length = len(A)
    remainder = K % length
    if not remainder:
        return A

    return A[-remainder:] + A[:length - remainder]
