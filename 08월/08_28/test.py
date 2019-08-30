mi = 20
input_num = 0
queue = []

while mi > 0:
    input_num += 1
    print('==>{}번 학생 입장해서 줄을 선다'.format(input_num))

    queue.append((input_num, 1))
    student_id, num = queue.pop(0)

    print('{}번 학생 : 줄에서 나와'.format(student_id))
    print('학생 줄 : {}'.format(queue))

    if mi > num:
        mi -= num
        print('{}번 학생 : 선생님에서 사탕 {}개를 받는다.'.format(student_id, num))
        print('===== 남은 사탕의 개수는 {}개다.'.format(mi))
        print()
        print('{}번 학생 다시 줄을 선다'.format(student_id))
        queue.append((student_id, num+1))
    else:
        print('{}번 학생 : 선생님에서 사탕 {}개를 받는다.'.format(student_id, mi))
        print('===== 남은 사탕의 개수는 0개다.')
        print('마지막으로 사탕을 받은 학생은 {}번이다.'.format(student_id))
        mi = 0



