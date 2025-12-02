#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <numeric>

using namespace std;

vector<string> split_string(string input_string, char delimiter)
{
    stringstream input_stream(input_string);
    string segment;
    vector<string> seglist;

    while (getline(input_stream, segment, delimiter))
    {
        seglist.push_back(segment);
    }

    return seglist;
}

void get_invalid_id_1(string input_file)
{

    ifstream infile(input_file);
    stringstream buffer;

    buffer << infile.rdbuf();
    string line = buffer.str();

    infile.close();

    stringstream id_ranges(line);
    string id_range;

    vector<long long> invalid_id_vector;

    while (getline(id_ranges, id_range, ','))
    {
        //cout << id_range << '\n';
        vector<string> ids = split_string(id_range, '-');
        string first_id = ids.front();
        string last_id = ids.back();

        cout << "Last ID: " + last_id << '\n';

        vector<long long> invalid_ids;

        for (long long id = stoll(first_id); id <= stoll(last_id); id++) {
            string id_string = to_string(id);
            /*cout << "ID: " + id_string 
            + " ID string length: " 
            + to_string(id_string.length()) << '\n';*/

            if (id_string.substr(0, id_string.length()/2)
            .compare(id_string.substr(id_string.length()/2, 
            id_string.length() - id_string.length()/2)) == 0) {
                invalid_ids.push_back(id);
            }
        }

        if (invalid_ids.size() > 0) {
            cout << id_range + " has " +
            to_string(invalid_ids.size()) + 
            " invalid IDs, ";
            for (long long i = 0; i < invalid_ids.size(); i++) {
                if (i > 0) {
                    cout << ", ";
                }
                cout << invalid_ids[i];
            }
            cout << '\n';
        }

        invalid_id_vector.insert(invalid_id_vector.end(),
        invalid_ids.begin(), invalid_ids.end());
    }
    cout << "The rest of the ranges contain no invalid IDs." << '\n';

    long long sum_ids = accumulate(invalid_id_vector.begin(),
    invalid_id_vector.end(), 0LL);

    cout << "Adding up all the invalid IDs produces "
    + to_string(sum_ids) << '\n';

}

int main()
{
    string sample_input = "sample_input.txt";
    string input = "input.txt";
    string test_input = "test_input.txt";

    //get_invalid_id_1(sample_input);
    get_invalid_id_1(input);
}