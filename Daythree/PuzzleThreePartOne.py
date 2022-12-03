lowercase = list(map(chr, range(97, 123)))
uppercase = [x.upper() for x in lowercase]
lowercasenums = list(range(1, 27))
uppercasenums = list(range(27, 53))

lower_dict = dict(zip(lowercase, lowercasenums))
upper_dict = dict(zip(uppercase, uppercasenums))
master_dict = lower_dict | upper_dict

def compare(stringa, stringb):
    for x, y in zip(stringa, stringb):
        if x in stringb:
            return x

def main():

    with open('input.txt') as f:
        text = f.read()
        myarray = text.split("\n")
        list_of_scores = []
        for line in myarray:
            firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
            error_item = compare(firstpart, secondpart)
            score = master_dict[error_item]
            list_of_scores.append(score)
        print(sum(list_of_scores))



    return None

if __name__ == "__main__":
    main()