a = 'UUUUUUUUUUUUUUUUUU'


vector = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}


def is_wall(p_x, p_y):
    if -5 <= p_x <= 5 and -5 <= p_y <= 5:
        return True
    return False


def solution(dirs):
    move_map = dict()
    center = [0, 0]
    for char in dirs:
        move = vector[char]
        temp = center.copy()
        center[0] += move[0]
        center[1] += move[1]
        if is_wall(*center):
            b = tuple(temp + center)
            print(b)
            move_map[b] = 1
        else:
            center[0] -= move[0]
            center[1] -= move[1]
    answer = len(move_map)
    return answer


print(solution(a))