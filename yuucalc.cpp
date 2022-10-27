#include <iostream>
using namespace std;

int main()
{
    float a, b;
    cout << "File Size (GB): ";
    cin >> a;
    cout << "Download Speed (Mbit): ";
    cin >> b;
    float c = (8000 / (b * 1000) * (a * 1000)) / 3600;
    cout << "Result: " << c << "h" << endl;
}
