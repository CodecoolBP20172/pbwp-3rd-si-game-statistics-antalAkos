
# Printing functions



def load_list(file_name):
    game_list = []
    with open(file_name) as map:
        for row in map:
            game_list.append(list(row.strip().split('\t')))
<<<<<<< HEAD
    print(game_list)
    return game_list



def count_games(file_name):
    games_number = load_list(file_name)
    game_count = len(games_number)
    print(game_count)
    return game_count
=======
    return game_list
load_list('/home/akos/codecool/pbwp-3rd-si-game-statistics-antalAkos/game_stat.txt')

def count_games(file_name):
    games_number = load_list(file_name)
    return len(games_number)


count_games('/home/akos/codecool/pbwp-3rd-si-game-statistics-antalAkos/game_stat.txt')
>>>>>>> 2129c97ce0114cd713d3148cf9c0e658e44dfc66


def decide(file_name, year):
    game_list = load_list(file_name)
    for game in game_list:
        if game[2] == str(year):
<<<<<<< HEAD
                print('True')
                return True
    print('False')
    return False


=======
                return True
    return False



print(decide('/home/akos/codecool/pbwp-3rd-si-game-statistics-antalAkos/game_stat.txt', 2004))

>>>>>>> 2129c97ce0114cd713d3148cf9c0e658e44dfc66
def get_latest(file_name):
    years = []
    game_list = load_list(file_name)
    for game in game_list:
        years.append(game[2])
    latest = int(years.index(max(years)))
<<<<<<< HEAD
    print(game_list[latest][0])
    return game_list[latest][0]


=======
    return game_list[latest][0]


get_latest('/home/akos/codecool/pbwp-3rd-si-game-statistics-antalAkos/game_stat.txt')


>>>>>>> 2129c97ce0114cd713d3148cf9c0e658e44dfc66
def count_by_genre(file_name, genre):
    genres = []
    game_list = load_list(file_name)
    for game in game_list:
        if game[3] == genre:
            genres.append(game[3])
<<<<<<< HEAD
    print(len(genres))
    return len(genres)


=======
    return len(genres)


count_by_genre('/home/akos/codecool/pbwp-3rd-si-game-statistics-antalAkos/game_stat.txt', 'RPG')

>>>>>>> 2129c97ce0114cd713d3148cf9c0e658e44dfc66
def get_line_number_by_title(file_name, title):
    game_list = load_list(file_name)
    for game in game_list:
        if game[0] == title:
<<<<<<< HEAD
            line_number = game_list.index(game) + 1
            print(line_number)
            return line_number
=======
            return game_list.index(game) + 1

''''
def sort_abc(file_name):
    titles = []
    game_list = load_list(file_name)
    for game in game_list:
        titles.append(game[0])
    for title in titles:
        for letter in title:
            while title <= titles[len(titles)- 1]:
                if title[letter] < title[letter + 1]:
                    temp = letter + 1
                    '''



sort_abc('/home/akos/codecool/pbwp-3rd-si-game-statistics-antalAkos/game_stat.txt')


print(get_line_number_by_title('/home/akos/codecool/pbwp-3rd-si-game-statistics-antalAkos/game_stat.txt', 'Doom 3'))
>>>>>>> 2129c97ce0114cd713d3148cf9c0e658e44dfc66
