from parseInput import parseInput3

def isGameFeasible(game):
    config = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for sub_set in game:
        actual = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for item in sub_set.split(','):
            actual[item.split()[1].strip()] += int(item.split()[0]) 
            if actual[item.split()[1].strip()] > config[item.split()[1].strip()]:
                return False    
    return True

if __name__ == "__main__":
    games = parseInput3()
    id_sum = 0
    for key in games.keys():
        if isGameFeasible(games[key]):
            id_sum += int(key.split(' ')[-1])
        else:
            continue
    print(id_sum)
