
with open('InputforPuzzleOne.txt') as f:

    text = f.read()
    myarray = text.split("\n\n")
     
    list_of_sums = []
    for line in myarray:
        lower_list = line.split("\n")
        lower_list = list(map(int, lower_list))
        sums = sum(lower_list)
        list_of_sums.append(sums)

    num_max_cals_elf = max(list_of_sums)
    print(f'Biggest calories: {num_max_cals_elf}')

    sorted_sums_desc = sorted(list_of_sums, reverse=True)
    topthree = sorted_sums_desc[:3]
    sum_top_three = sum(topthree)
    print(f'Sum of top three: {sum_top_three}')
