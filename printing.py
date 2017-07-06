
# Printing functions



def load_list(file_name):
    game_list = []
    with open(file_name) as map:
        for row in map:
            game_list.append(list(row.strip().split('\t')))
    print(game_list)
    return game_list



def count_games(file_name):
    games_number = load_list(file_name)
    game_count = len(games_number)
    print(game_count)
    return game_count


def decide(file_name, year):
    game_list = load_list(file_name)
    for game in game_list:
        if game[2] == str(year):
                print('True')
                return True
    print('False')
    return False


def get_latest(file_name):
    years = []
    game_list = load_list(file_name)
    for game in game_list:
        years.append(game[2])
    latest = int(years.index(max(years)))
    print(game_list[latest][0])
    return game_list[latest][0]


def count_by_genre(file_name, genre):
    genres = []
    game_list = load_list(file_name)
    for game in game_list:
        if game[3] == genre:
            genres.append(game[3])
    print(len(genres))
    return len(genres)


def get_line_number_by_title(file_name, title):
    game_list = load_list(file_name)
    for game in game_list:
        if game[0] == title:
            line_number = game_list.index(game) + 1
            print(line_number)
            return line_number
