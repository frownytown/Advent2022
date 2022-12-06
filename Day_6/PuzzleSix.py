def main():

    with open('input.txt') as f:
        text = f.read()
        for i in range(len(text)):
            part_one_set = set([text[i], text[i-1], text[i-2], text[i-3]])
            if (i >= 3) and (len(part_one_set) == 4):
                print(f"Part one: {part_one_set}, {i+1}")
                break
        for i in range(len(text)):
            part_two_set = set([text[i], text[i-1], text[i-2], text[i-3], text[i-4], text[i-5], text[i-6], text[i-7],
            text[i-8], text[i-9], text[i-10], text[i-11],text[i-12], text[i-13]])
            if (i >= 13) and (len(part_two_set) == 14):
                print(f"Part two: {part_two_set}, {i+1}")
                break


    return None


if __name__ == "__main__":
    main()
