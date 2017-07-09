
# Report functions


import csv


def load_list(file_name):
    game_list = []
    with open(file_name) as stats:
        for row in stats:
            game_list.append(list(row.strip().split('\t')))
    game_list_csv = []
    if '.csv' in file_name:
        for sublist in game_list:
            game_list_csv.append(sublist[0].split(','))
        return game_list_csv
    else:
        return game_list


def most_played_func(file_name, pos):
    most_played_list = []
    game_list = load_list(file_name)
    for game in game_list:
        most_played_list.append(float(game[pos]))
    return most_played_list

#  1


def get_most_played(file_name):
    most_played_list = most_played_func(file_name, 1)
    game_list = load_list(file_name)
    most_played = int(most_played_list.index(max(most_played_list)))
    most_played_game = game_list[most_played][0]
    return most_played_game

#  2


def sum_sold(file_name):
    most_played_list = most_played_func(file_name, 1)
    return sum(most_played_list)

#  3


def get_selling_avg(file_name):
    most_played_list = most_played_func(file_name, 1)
    average = sum(most_played_list)/len(most_played_list)
    return average

#  4


def count_longest_title(file_name):
    titles = []
    title_list = load_list(file_name)
    for title in title_list:
        titles.append(len(title[0]))
    return(max(titles))

#  5


def get_date_avg(file_name):
    most_played_list = most_played_func(file_name, 2)
    average = round(sum(most_played_list)/len(most_played_list), 0)
    return average

#  6


def get_game(file_name, title):
    game_list = load_list(file_name)
    for game in game_list:
        if title in game:
            game[1] = float(game[1])
            game[2] = int(game[2])
            return game

#  7


def count_grouped_by_genre(file_name):
    genres = []
    game_list = load_list(file_name)
    for game in game_list:
        genres.append(game[3])
    genre_dict = {}
    for item in genres:
        genre_dict[item] = genres.count(item)
    return(genre_dict)

#  8


def get_date_ordered(file_name):
    dates_dict = {}
    game_list = load_list(file_name)
    for game in game_list:
        dates_dict[game[0]] = int(game[2])
    order = [v[0] for v in sorted(dates_dict.items(), key=lambda kv: (-kv[1], kv[0]))]
    return order
