
import os 
input_file = open(os.getcwd() + '/input.txt', 'r').read().split('\n')
sample_input_file = open(os.getcwd() + '/sample_input.txt', 'r').read().split('\n')
#print(input_file)

sample_input_array = ["L50", "R1000"]

def get_password_1(input_file):
    num = 50

    password = 0

    print("The dial starts by pointing at 50.")
    for line in input_file:
        direction = line[0]
        offset = int(line[1:])
        if direction == "L":
            num = (num - offset) % 100
        elif direction == "R":
            num = (num + offset) % 100
        

        print(f"The dial is rotated {line} to point at {num}.")
        if num == 0:
            password += 1
    print("The password is " + str(password))


def get_password_2(input_file):
    num = 50

    password = 0

    print("The dial starts by pointing at 50.")
    for line in input_file:
        print("---")
        direction = line[0]
        offset = int(line[1:])
        clicks = 0
        starting_num = num

        if direction == "L":
            #Calc for L is slightly funky because of negative offset, so check for starting number and ending number

            diff = num - offset
            num = (diff) % 100
            clicks += abs((diff) // 100)
            
            if starting_num == 0:
                clicks -= 1
            if num == 0:
                clicks += 1

        elif direction == "R":
            diff = num + offset
            num = (diff) % 100
            clicks = abs((diff) // 100)
        
        

        print(f'The dial is rotated {line} to point at {num}.')

        if clicks != 0:
            print(f'During this rotation, it points at 0 x{clicks} time(s).')
        password += clicks


    print("The password is " + str(password))

#get_password_2(sample_input_array)

#get_password_2(sample_input_file)

get_password_2(input_file)