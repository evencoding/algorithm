def solution(new_id):
    result = ''
    # 1
    new_id = new_id.lower()
    # 2
    for word in new_id:
        if word.isalnum() or word in '-_.':
            result += word
    # 3
    while '..' in result:
        result = result.replace('..', '.')
    # 4
    if result[0] == '.' and len(result) > 0:
        result = result[1:]
    if result[-1] == '.' and len(result) > 0:
        result = result[:-1]
    # 5
    if len(result) == 0:
        result = 'a'
    # 6
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    # 7
    if len(result) <= 2:
        while len(result) < 3:
            result += result[-1]

    return result
