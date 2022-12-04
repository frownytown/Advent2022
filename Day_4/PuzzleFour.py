
def get_num_range_from_str(string1, string2):

    range_nums_1, range_nums_2  = string1.split('-'), string2.split('-')
    section1nums  = list(range(int(range_nums_1[0]), int(range_nums_1[1])+1)) 
    section2nums = list(range(int(range_nums_2[0]), int(range_nums_2[1])+1))

    return section1nums, section2nums

def main():

    
    with open('input.txt') as f:
        text = f.read()
        myarray = text.split("\n")
        partonecounter = 0
        parttwocounter = 0
        for line in myarray:
            string1, string2 = line.split(',')
            section1nums, section2nums = get_num_range_from_str(string1, string2)
            if all(item in section1nums for item in section2nums) or all(item in section2nums for item in section1nums):
                partonecounter += 1
            if any(item in section1nums for item in section2nums):
                parttwocounter += 1
        print(f"Part one answer: {partonecounter}")
        print(f"Part two answer: {parttwocounter}")

    return None

if __name__ == "__main__":
    main()