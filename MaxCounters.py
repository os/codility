from collections import defaultdict


def solution(N, A):
    max_counter = previous_max_counter = 0
    max_counter_command = N + 1
    counters = defaultdict(int)
    for index in A:
        if 1 <= index <= N:
            counters[index - 1] += 1
            counter = counters[index - 1]
            if counter > max_counter:
                max_counter = counter
        elif index == max_counter_command:
            previous_max_counter = max_counter
            counters = defaultdict(lambda: previous_max_counter, {})

    return [counters[i] for i in xrange(N)]
