# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, splitter=','):
    str_set_1 = set(str_1.split(splitter))
    common_participants = list(str_set_1.intersection(str_2.split(splitter)))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, splitter='|'))