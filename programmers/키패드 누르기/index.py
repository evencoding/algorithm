def solution(numbers, hand):
    answer = ''
    key = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left = key['*']
    right = key['#']

    for i in numbers:
        now = key[i]

        if i in [1, 4, 7]:
            answer += 'L'
            left = now
        elif i in [3, 6, 9]:
            answer += 'R'
            right = now
        else:
            left_d = 0
            right_d = 0

            for l, r, n in zip(left, right, now):
                left_d += abs(l - n)
                right_d += abs(r - n)

            if left_d > right_d:
                answer += 'R'
                right = now
            elif right_d > left_d:
                answer += 'L'
                left = now
            else:
                if hand == 'right':
                    answer += 'R'
                    right = now
                else:
                    answer += 'L'
                    left = now
    return answer
