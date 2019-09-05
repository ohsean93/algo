name_dict = dict()
log_dict = []

record = [
    "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
    "Enter uid1234 Prodo", "Change uid4567 Ryan"
]

for log in record:
    log_list = log.split()
    if log_list[0] == 'Enter':
        user_id = log_list[1]
        user_name = log_list[2]
        name_dict[user_id] = user_name
        log_dict.append((1, user_id))
    elif log_list[0] == 'Leave':
        user_id = log_list[1]
        log_dict.append((0, user_id))
    elif log_list[0] == 'Change':
        user_id = log_list[1]
        user_name = log_list[2]
        name_dict[user_id] = user_name

answer = []
for checker, user_id in log_dict:
    if checker:
        answer.append('{}님이 들어왔습니다.'.format(name_dict[user_id]))
    else:
        answer.append('{}님이 나갔습니다.'.format(name_dict[user_id]))

print(answer)