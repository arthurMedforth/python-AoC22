from parseInput import parseInput3

def isGameFeasible(game):
    config = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sets = []
    feasible_bool = True
    for sub_set in game:
        actual = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for item in sub_set.split(','):
            actual[item.split()[1].strip()] += int(item.split()[0])
            if actual[item.split()[1].strip()] > config[item.split()[1].strip()]:
                feasible_bool = False
        sets.append(actual)
    return feasible_bool, sets

if __name__ == "__main__":
    games = parseInput3()
    id_sum = 0
    power_sum = 0
    for key in games.keys():
        feasible_bool, sets = isGameFeasible(games[key])
        power_sum += max([set['red'] for set in sets]) * max([set['green'] for set in sets]) * max([set['blue'] for set in sets])
        if feasible_bool:
            id_sum += int(key.split(' ')[-1])
        else:
            continue
    print(power_sum)
    print(id_sum)
