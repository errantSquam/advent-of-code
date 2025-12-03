import os 
input_file = open(os.getcwd() + '/input/input.txt', 'r').read().split('\n')
sample_input_file = open(os.getcwd() + '/input/sample_input.txt', 'r').read().split('\n')

def solve_largest_joltage_1(battery_map):
    for digit_one in reversed(range(1, 10)):
        for digit_one_index in battery_map[digit_one]:
            for digit_two in reversed(range(1,10)):
                digit_two_indexes = battery_map[digit_two]
                return_indexes = [i for i in digit_two_indexes if i > digit_one_index]
                if len(return_indexes) > 0:
                    return str(digit_one) + str(digit_two)
                        
def solve_battery_1(input_file):
    
    joltage_array = []
    for bank in input_file:
        battery_map = {}
        largest_joltage = 0

        for i in range(1, 10):
            battery_map[i] = []

        #print(battery_map)
        for battery_index in range(len(bank)):
            current_battery = bank[battery_index]
            battery_map[int(current_battery)].append(battery_index)

        largest_joltage = solve_largest_joltage_1(battery_map)
        joltage_array.append(int(largest_joltage))

        print(f"in {bank}, you can make the largest joltage possible, which is {largest_joltage}.")

    print(f"The total output joltage is {sum(joltage_array)}.")

def solve_largest_joltage_2(bank, battery_map, largest_joltage_array):
    #credit to kimmy for the idea
    if len(largest_joltage_array) == 12:
        return largest_joltage_array
    
    for digit in reversed(range(1, 10)):
            for digit_index in battery_map[digit]:
                if digit_index + 11-len(largest_joltage_array) < len(bank) and \
                    (len(largest_joltage_array) == 0 or digit_index > largest_joltage_array[-1][1]):
                    largest_joltage_array.append((digit, digit_index))
                    return solve_largest_joltage_2(bank, battery_map, largest_joltage_array)
    
    return []

    




def solve_battery_2(input_file):
    
    joltage_array = []
    for bank in input_file:
        battery_map = {}
        largest_joltage = 0

        for i in range(1, 10):
            battery_map[i] = []

        #print(battery_map)
        for battery_index in range(len(bank)):
            current_battery = bank[battery_index]
            battery_map[int(current_battery)].append(battery_index)

        largest_joltage_pairs = solve_largest_joltage_2(bank, battery_map, [])
        largest_joltage = ''.join([str(i[0]) for i in largest_joltage_pairs])
        joltage_array.append(int(largest_joltage))

        print(f"in {bank}, you can make the largest joltage possible, which is {largest_joltage}.")

    print(f"The total output joltage is {sum(joltage_array)}.")

#solve_battery_2(sample_input_file)
solve_battery_2(input_file)

