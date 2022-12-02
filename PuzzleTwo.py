
pointvalues = {'Y': 2, 'X': 1, 'Z': 3, 'Loss': 0, 'Draw': 3, 'Win': 6}


opponent_value_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
my_value_dict = {'Rock': 'X', 'Paper': 'Y', 'Scissors': 'Z'}
strat_dict = {'X': 'Loss', 'Y': 'Draw', 'Z': 'Win'}


def score_game(opponent_choice, strat):
    print(opponent_value_dict[opponent_choice], strat_dict[strat])
    opponent_val = opponent_value_dict[opponent_choice]
    strat_val = strat_dict[strat]
    if opponent_val == 'Rock' and strat_val == 'Loss':
        mychoice = my_value_dict['Scissors']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Rock' and strat_val == 'Draw':
        mychoice = my_value_dict['Rock']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Rock' and strat_val == 'Win':
        mychoice = my_value_dict['Paper']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Paper' and strat_val == 'Loss':
        mychoice = my_value_dict['Rock']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Paper' and strat_val == 'Draw':
        mychoice = my_value_dict['Paper']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Paper' and strat_val == 'Win':
        mychoice = my_value_dict['Scissors']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Scissors' and strat_val == 'Loss':
        mychoice = my_value_dict['Paper']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Scissors' and strat_val == 'Draw':
        mychoice = my_value_dict['Scissors']
        points = pointvalues[strat_val] + pointvalues[mychoice]
    elif opponent_val == 'Scissors' and strat_val == 'Win':
        mychoice = my_value_dict['Rock']
        points = pointvalues[strat_val] + pointvalues[mychoice]

    return points

def main():

    with open('input.txt') as f:

        text = f.read()
        myarray = text.split("\n")
        list_of_scores = []
        for line in myarray:
            lower_list = line.split()
            scoreing = score_game(lower_list[0], lower_list[1])
            list_of_scores.append(scoreing)
        total_score = sum(list_of_scores)
        print(total_score)
        
    return None


if __name__ == "__main__":
    main()