list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
total = len(list_players) // 2
team1 = list_players[:total]
team2 = list_players[total:]
print(team1)
print(team2)
