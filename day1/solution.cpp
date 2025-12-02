#include <iostream>
#include <fstream>

using namespace std;


inline int positive_modulo(int i, int n) {
    return (i % n + n) % n;
}

void get_password_1(string input_file) {

    string line;

    ifstream input(input_file);

    int num = 50;
    int password = 0;


    cout << "The dial starts by pointing at 50." << '\n';

    while (getline (input, line)) {
        string direction = line.substr(0, 1);
        int offset = std::stoi(line.substr(1, line.size() - 1));

        if (direction.compare("L") == 0) {
            num = positive_modulo((num - offset), 100);
        }

        else if (direction.compare("R") == 0) {
            num = positive_modulo((num + offset), 100);
        }

        cout << "The dial is rotated " + line 
        + " to point at " + to_string(num) << '\n';

        if (num == 0) {
            password += 1;
        }
    }

    cout << "The password is " + to_string(password) << '\n';
    
    input.close();

};

void get_password_2(string input_file) {
    string line;

    ofstream write_file;

    write_file.open("output/answerfile_cpp.txt");

    ifstream input(input_file);

    int num = 50;
    int password = 0;


    write_file << "The dial starts by pointing at 50." << '\n';


    while (getline (input, line)) {
        write_file << "---" << '\n';
        //cout << line << '\n';
        string direction = line.substr(0, 1);
        
        //cout << "Direction is " + direction << '\n';
        int offset = std::stoi(line.substr(1, line.size() - 1));

        int clicks = 0;
        int diff = 0;
        int starting_num = num;

        if (direction.compare("L") == 0) {
            diff = num - offset;
            num = positive_modulo((diff), 100);
            clicks += abs(diff)/ 100;

            //Account for negative rotation.
            if (diff < 0) {
                clicks += 1;
            }
            
            if (starting_num == 0) {
                clicks -= 1;
            }

            //Check if it's not a full rotation
            //THEN count it landing on 0.
            if (num == 0 && abs(diff)/ 100 == 0) {
                clicks += 1;
            }
        }

        else if (direction.compare("R") == 0) {
            diff = num + offset;
            num = positive_modulo((diff), 100);
            clicks += abs((diff)) / 100;
        }

        write_file << "The dial is rotated " + line 
        + " to point at " + to_string(num) + '.' << '\n';

        if (clicks != 0) {
            write_file << "During this rotation, it points at zero " + 
            to_string(clicks) + " time(s)." 
            << '\n';
        }
        password += clicks;
    }

    write_file << "The password is " + to_string(password) << '\n';
    write_file.close();
    input.close();    

};


int main() {


    string sample_input = "input/sample_input.txt";
    string input = "input/input.txt";
    string test_input = "input/test_input.txt";

    //get_password_2(sample_input);
    //get_password_2(test_input);
    get_password_2(input);


}