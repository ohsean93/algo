line_1 = ['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']
line_2 = [
    '2016-09-15 20:59:57.421 0.351s',
    '2016-09-15 20:59:58.233 1.181s',
    '2016-09-15 20:59:58.299 0.8s',
    '2016-09-15 20:59:58.688 1.041s',
    '2016-09-15 20:59:59.591 1.412s',
    '2016-09-15 21:00:00.464 1.466s',
    '2016-09-15 21:00:00.741 1.581s',
    '2016-09-15 21:00:00.748 2.31s',
    '2016-09-15 21:00:00.966 0.381s',
    '2016-09-15 21:00:02.066 2.62s'
]
line_3 = ['2016-09-15 00:00:00.000 3s']


def solution(lines):
    all_time = [0] * 86400001

    max_num = 0
    for time_str in lines:
        a, b = change_time(time_str)
        for num in range(max(0, a-1001), b+1):
            p = all_time[num] = all_time[num] + 1
            if p > max_num:
                max_num = p

    return max_num


def change_time(str_time):
    date, time, lens = str_time.split()  # type: (str, str, str)
    h, m, s = time.split(':')  # type: (str, str, str)
    start_time = int(h) * 3600 * 1000 + int(m) * 60000 + int(s.replace('.', ''))
    temp = lens.replace('s', '').split('.')
    if len(temp) == 2:
        end_time = start_time - int(temp[0]) * 1000 - int(temp[1]) * (10 ** (3 - len(temp[1])))
    else:
        end_time = start_time - int(temp[0]) * 1000
    return end_time, start_time


print(solution(line_3))
