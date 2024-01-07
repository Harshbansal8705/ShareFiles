#include <iostream>

using namespace std;

int main()
{
    string str1 = "EFGABC", str2 = "ABC";
    if (str1.length() > str2.length())
        swap(str1, str2);
    while (str1.compare(str2))
    {
        string temp = str1;
        if (str1.compare(str2.substr(0, str1.length())))
        {
            cout << "" << endl;
            break;
        }
        str1 = str2.substr(str1.length());
        str2 = temp;
        if (str1.length() > str2.length())
            swap(str1, str2);
        if (str1.length() == 0)
        {
            cout << "" << endl;
            break;
        }
    }
    cout << str1 << endl;

    return 0;
}