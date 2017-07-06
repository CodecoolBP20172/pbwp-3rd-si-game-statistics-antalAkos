
# Report functions


def load_list(file_name):
    game_list = []
    with open(file_name) as map:
        for row in map:
            game_list.append(list(row.strip().split('\t')))
    return game_list


# 1
def count_games(file_name):
    games_number = load_list(file_name)
    return len(games_number)


# 2
def decide(file_name, year):
    game_list = load_list(file_name)
    for game in game_list:
        if game[2] == str(year):
                return True
    return False


# 3
def get_latest(file_name):
    years = []
    game_list = load_list(file_name)
    for game in game_list:
        years.append(game[2])
    latest = int(years.index(max(years)))
    return game_list[latest][0]


# 4
def count_by_genre(file_name, genre):
    genres = []
    game_list = load_list(file_name)
    for game in game_list:
        if game[3] == genre:
            genres.append(game[3])
    return len(genres)


# 5
def get_line_number_by_title(file_name, title):
    game_list = load_list(file_name)
    for game in game_list:
        if game[0] == title:
            return game_list.index(game) + 1
