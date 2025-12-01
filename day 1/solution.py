
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
            num -= offset
        elif direction == "R":
            num += offset

        while num < 0:
            num = num + 100

        while num > 99:
                num = num - 100
        
        print(f"The dial is rotated {line} to point at {num}.")

        if num == 0:
            password += 1
    print("The password is " + str(password))


def get_password_2(input_file):
    num = 50

    password = 0

    print("The dial starts by pointing at 50.")
    for line in input_file:

        print('\n')
        direction = line[0]
        offset = int(line[1:])

        starting_num = num
        clicks = 0 
        final_clicks = 0

        isFirstLoop = True

        if direction == "L":
            num -= offset
        elif direction == "R":
            num += offset

        while num < 0:
            num = num + 100
            if not (starting_num == 0 and isFirstLoop):
                clicks +=1
            isFirstLoop = False

        while num > 99:
            num = num - 100
            if not (starting_num == 0 and isFirstLoop):
                clicks +=1
            isFirstLoop = False

        
        '''
        Do not count if it ends at 0.
        if num == 0 and clicks == 0:
            clicks += 1
        '''

        if num == 0:
            final_clicks += 1
            if clicks > 0:
                clicks -=1


        password += clicks + final_clicks
        
        print(f'The dial is rotated {line} to point at {num}.')

        if final_clicks != 0:
            print(f'It ended at 0 on the end of the rotation.')

            if final_clicks != 1:
                print(f"Hmm, something's weird here. Final_clicks was triggered {final_clicks} times.")

        if clicks != 0:
            print(f'During this rotation, it points at 0 x{clicks} time(s).')


    print("The password is " + str(password))

#get_password_2(sample_input_array)

#get_password_2(sample_input_file)

get_password_2(input_file)