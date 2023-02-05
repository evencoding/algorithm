def solution(lottos, win_nums):
    cnt = 0
    for n in lottos:
        if n in win_nums:
            cnt += 1
    maxWin = 7-lottos.count(0)-cnt if cnt+lottos.count(0) >= 2 else 6
    minWin = 7-cnt if cnt >= 2 else 6
    return [maxWin, minWin]
