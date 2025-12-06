from functools import reduce
import os 
import numpy as np

import re


input_file = open(os.getcwd() + '/input/input.txt', 'r').read().split('\n')
sample_input_file = open(os.getcwd() + '/input/sample_input.txt', 'r').read().split('\n')


def parse_problem(input):
    input = [[j for j in i.split(' ') if j != ''] for i in input]
    return input

def parse_operator_index(operatorList):
    return [m.start() for m in re.finditer(r'\*|\+', operatorList)]

def solve_problem_1(input):
    input = parse_problem(input)
    operatorList = input[-1]

    solutions = []

    for number_index in range(len(input) - 1):
        for problem_index in range(len(input[0])):

            #Add in if doesn't exist
            currentNum = int(input[number_index][problem_index])
            currentOperator = operatorList[problem_index]

            if len(solutions) -1 < problem_index:
                solutions.append(currentNum)
                continue

            if currentOperator == "*":
                solutions[problem_index] *= currentNum 

            elif currentOperator == "+":
                solutions[problem_index] += currentNum
    
    print(solutions)
    print(f"The total sum is {sum(solutions)}.")
            
def solve_problem_2_old(input):
    input = parse_problem(input)
    operatorList = input[-1]
    matrices = []
    for number_index in range(len(input) - 1):
        for problem_index in range(len(input[0])):

            #Add in if doesn't exist
            currentNum = int(input[number_index][problem_index])
            if len(matrices) -1 < problem_index:
                matrices.append(
                    {
                        "matrixList": [currentNum],
                        "maxLen": len(str(currentNum)),
                        "operator": operatorList[problem_index]
                    }
                                )
                continue
            matrices[problem_index]["matrixList"].append(currentNum)
            if (len(str(currentNum))) > matrices[problem_index]["maxLen"]:
                matrices[problem_index]["maxLen"] = len(str(currentNum))

    solutions = []
    for matrix_index in range(len(matrices)):
        matrix = matrices[matrix_index]
        newMatrix = []
        for number in matrix["matrixList"]:
            if len(str(number)) <= matrix["maxLen"]:
                diff = matrix["maxLen"] - len(str(number))
                number = [int(i) for i in list(str(number))]
                number = [-1] * diff + number
            

            newMatrix.append(number)

        newMatrix = np.matrix(newMatrix)
        print("--")
        print(newMatrix)
        print(newMatrix.transpose())
        transformedNum = [int(''.join([str(j) for j in i if j != -1])) for i in np.asarray(newMatrix.transpose())]


        print(transformedNum)

        solution = 0
        if matrix["operator"] == "*":
            solution = reduce(lambda x,y: x*y, transformedNum)
        elif matrix["operator"] == "+":
            solution = sum(transformedNum)

        print(f"Operator: {matrix["operator"]}, solution: {solution}")
        solutions.append(solution)

    print(f"Solutions are: {solutions}")
    return 

def solve_problem_2(input):
    operatorList = input[-1]
    input = [row + ' ' for row in input]
    operatorIndices = parse_operator_index(operatorList)
    parts = [[row[i:j] for i,j in zip(operatorIndices, operatorIndices[1:]+[None])] for row in input]
    parts = parts[0:len(parts)-1]
    parts = [[j[0:len(j)-1] for j in i] for i in parts]


    parts = np.array(parts).T.tolist()

    operatorList = [i for i in input[-1].split(" ") if i != ""]

    solutions = []

    for part_index in range(len(parts)):
        part = parts[part_index]
        operator = operatorList[part_index]
        newNums = ['' for i in range(len(part[0]))]
        for number in part:
            for digit in range(len(number)):
                #print(digit)
                currentDigit = number[digit]
                #print(f"Current Digit: {currentDigit}")
                if currentDigit != ' ':
                    newNums[digit] += currentDigit

        newNums = [int(i) for i in newNums]

        solution = 0
        if operator == "*":
            solution = reduce(lambda x,y: x*y, newNums)
            print(f"{newNums} multiply to form {solution}")
        elif operator == "+":
            solution = sum(newNums)        
            print(f"{newNums} add to form {solution}")

        solutions.append(solution)
                
    print(f"The final sum is {sum(solutions)}.")

#solve_problem_2(sample_input_file)
solve_problem_2(input_file)