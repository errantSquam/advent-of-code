import os 
input_file = open(os.getcwd() + '/input/input.txt', 'r').read().split('\n')
sample_input_file = open(os.getcwd() + '/input/sample_input.txt', 'r').read().split('\n')


def get_fresh_1(input):
    fresh_ranges = []

    fresh_ingredients = 0

    checkFresh = True
    for line in input:
        if line == "":
            checkFresh = False 
            continue

        if checkFresh:
            line = line.split("-")
            fresh_ranges.append([int(i) for i in line])

        else:
            ingredient = int(line)
            isFresh = False
            for fresh_range in fresh_ranges:
                if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
                    fresh_ingredients+=1 
                    isFresh = True
                    print(f"Ingredient ID {ingredient} is fresh because it falls into range {fresh_range[0]}-{fresh_range[1]}.")
                    break
            
            if not isFresh:
                print(f"Ingredient ID {ingredient} is spoiled.")

    print(f"{fresh_ingredients} of the available ingredient IDs are fresh.")


def get_fresh_2(input):
    fresh_ranges = []

    fresh_ingredients = 0

    checkFresh = True

    currentStart = None
    currentEnd = None

    input = input[:input.index('')]
    input = [[int(i) for i in  line.split("-")] for line in input]

    
    input.sort(key = lambda i:i[0])
    for line in input:
        if line == "":
            checkFresh = False 
            break

        if checkFresh:
            newStart = line[0]
            newEnd = line[1]

            #print(f"current: ({currentStart}-{currentEnd})")
            #print(f"new: {newStart} - {newEnd}")

            if currentStart == None:
                currentStart = newStart 

            if currentEnd == None:
                currentEnd = newEnd

            if newStart > currentEnd:
                fresh_ranges.append([currentStart, currentEnd])
                currentStart = newStart 
                currentEnd = newEnd 
                continue

            if newEnd > currentEnd:
                currentEnd = newEnd
    fresh_ranges.append([currentStart, currentEnd])

    #print(fresh_ranges)

    fresh_ingredients = sum([(i[1] - i[0] + 1) for i in fresh_ranges])
    print(f"{fresh_ingredients} of the available ingredient IDs are fresh.")

#get_fresh_1(sample_input_file)
#get_fresh_1(input_file)
#get_fresh_2(sample_input_file)
get_fresh_2(input_file)