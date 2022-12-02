
pointvalues = {'Y': 2, 'X': 1, 'Z': 3, 'Loss': 0, 'Draw': 3, 'Win': 6}


opponent_value_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
my_value_dict = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

def score_game(opponent_choice, my_choice):
    print(opponent_choice, my_choice)
    if opponent_value_dict[opponent_choice] == my_value_dict[my_choice]:
        gameResult = 'Draw'
        points = pointvalues[gameResult] + pointvalues[my_choice]
    elif opponent_choice == 'B' and my_choice == 'X':
        gameResult = 'Loss'
        points = pointvalues[gameResult] + pointvalues[my_choice]
    elif opponent_choice == 'C' and my_choice == 'X':
        gameResult = 'Win'
        points = pointvalues[gameResult] + pointvalues[my_choice]
    elif opponent_choice == 'A' and my_choice == 'Y':
        gameResult = 'Win'
        points = pointvalues[gameResult] + pointvalues[my_choice]
    elif opponent_choice == 'A' and my_choice == 'Z':
        gameResult = 'Loss'
        points = pointvalues[gameResult] + pointvalues[my_choice]
    elif opponent_choice == 'B' and my_choice == 'Z':
        gameResult = 'Win'
        points = pointvalues[gameResult] + pointvalues[my_choice]
    elif opponent_choice == 'C' and my_choice == 'Y':
        gameResult = 'Loss'
        points = pointvalues[gameResult] + pointvalues[my_choice]


    return gameResult, points





def main():

    with open('input.txt') as f:

        text = f.read()
        myarray = text.split("\n")
        list_of_scores = []
        for line in myarray:
            lower_list = line.split()
            scoreing = score_game(lower_list[0], lower_list[1])
            list_of_scores.append(scoreing[1])
            print(scoreing)
        total_score = sum(list_of_scores)
        print(total_score)

    return None


if __name__ == "__main__":
    main()