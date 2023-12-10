def extractInput():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    cards = {}
    for i in range(len(file_lines)):
        line = file_lines[i].strip()
        cards[int(line.split(':')[0][-4:].strip())] = [line.split(':')[1].split('|')[0].strip().split(' '),line.split(':')[1].split('|')[1].strip().split(' ')]
    for key in cards.keys():
        cards[key][0] = [int(el) for el in cards[key][0] if el != '']
        cards[key][1] = [int(el) for el in cards[key][1] if el != '']
    return cards

def part1(cards):
    winnings = []
    for key in cards.keys():
        winning_numbers = cards[key][0]
        my_numbers = cards[key][1]
        wins = []
        for num in winning_numbers:
            if num in my_numbers:
                wins.append(num)
        if len(wins) > 0:
            winnings.append(wins)
    answer = 0
    for win in winnings:
        if len(win) > 1:
            sub_ans = 1
            for i in range(0,len(win)-1):
                sub_ans = sub_ans * 2
            answer += sub_ans
        else:
            answer += 1
    return answer

def retrieveWonScratches(orig_cards, key, total_scratches):
    winning_numbers = cards[key][0]
    my_numbers = cards[key][1]
    wins = []
    for num in winning_numbers:
        if num in my_numbers:
            wins.append(num)
    total_scratches += len(wins)
    new_cards = {key+i+1: [] for i in range(0,len(wins))}
    for i, win in enumerate(wins):
        new_cards[key+i+1] = orig_cards[key+i+1]
    if len(new_cards.keys()) > 0:
        for _new_key in new_cards.keys():
            total_scratches = retrieveWonScratches(orig_cards, _new_key, total_scratches)
    return total_scratches

if __name__ == '__main__':
    cards = extractInput()
    cards_copy = cards
    total_scratches = 0
    #print(part1(cards))
    for _key in cards.keys():
        total_scratches = retrieveWonScratches(cards_copy, _key, total_scratches)
    print(total_scratches+len(cards.keys()))