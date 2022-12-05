from collections import defaultdict


def parsestacks(startingstacks):

    stacks = defaultdict(list)
    positions = {}
    for l in reversed(startingstacks.split("\n")):
        if not positions:
            for pos, stacknum in enumerate(l):
                if stacknum != " ":
                    positions[pos] = int(stacknum)
        else:
            for pos, stacknum in positions.items():
                if pos < len(l) and l[pos] != " ":
                    stacks[stacknum].append(l[pos])

    return stacks

def executeinstructions_partone(stacks, instructions):

    num_elements_moving = instructions[0]
    source = instructions[1]
    destination = instructions[2]

    for i in range(num_elements_moving):
        crate = stacks[source].pop()
        stacks[destination].append(crate)     

    return stacks

def executeinstructions_parttwo(stacks, instructions):

    num_elements_moving = instructions[0]
    source = instructions[1]
    destination = instructions[2]
    crate = stacks[source][len(stacks[source]) - num_elements_moving:]
    del stacks[source][len(stacks[source]) - num_elements_moving:]
    for element in crate:
        stacks[destination].append(element)

    return stacks

def calculate_top_values(stack):
        top_value = []
        for k,v in stack.items():
            top_value.append(v[-1])
        top = ''.join(top_value)
        return top


def main():

    with open('input.txt') as f:
        text = f.read()
        startingstacks, rearrangement = text.split("\n\n")
        print(startingstacks)
        starting_state_one = parsestacks(startingstacks)
        starting_state_two = parsestacks(startingstacks)


        instructions_list = rearrangement.split("\n")
        num_instructions = []
        for instructionstring in instructions_list:
            num_instruction = [
                int(s) for s in instructionstring.split() if s.isdigit()]
            num_instructions.append(num_instruction)
        for value in num_instructions:
            stacks_partone = executeinstructions_partone(starting_state_one, value)
            stacks_parttwo = executeinstructions_parttwo(starting_state_two, value)
        
        top_values_p1 = calculate_top_values(stacks_partone)
        top_values_p2 = calculate_top_values(stacks_parttwo)
        print(f"Part one top values: {top_values_p1}")
        print(f"Part two top values: {top_values_p2}")
        

    return None


if __name__ == "__main__":
    main()
