def create_dict():
    lowercase = list(map(chr, range(97, 123)))
    uppercase = [x.upper() for x in lowercase]
    lowercasenums = list(range(1, 27))
    uppercasenums = list(range(27, 53))

    lower_dict = dict(zip(lowercase, lowercasenums))
    upper_dict = dict(zip(uppercase, uppercasenums))
    master_dict = lower_dict | upper_dict
    return master_dict

def compare(string_list):

    for character in string_list[0]:
        if character in string_list[1]:
            if character in string_list[2]:
                return character

def main():

    master_dict = create_dict()

    with open('input.txt') as f:
        text = f.read()
        myarray = text.split("\n")
        groups = []
        list_of_scores = []
        for line in range(0, len(myarray), 3):
            groups.append(
                f'{myarray[line]} {myarray[line+1]} {myarray[line+2]}')
        for entry in groups:
            pool = entry.split(' ')
            commonvalue = compare(pool)
            score = master_dict[commonvalue]
            list_of_scores.append(score)
        print(sum(list_of_scores))

    return None


if __name__ == "__main__":
    main()