#include <iostream>
#include <vector>
using namespace std;

// Function to calculate the Euler's method
void euler(double (*y_der)(double, double), double a, double b, double t0, double y0, double h)
{
    int M = (int) ((b - a)/h);
    vector<double> y_arr{ y0 + h*(y_der(t0, y0)) };
    
    for (int i = 1; i < M; ++i)
    {
        y_arr.push_back(y_arr[i-1] + h*(y_der(i, y_arr[i-1])));
    }

    cout << "\nH is: " << h << endl;
    for (int i = 0; i < y_arr.size() ; i++ )
    {
        cout << i << " " <<  y_arr[i] << endl;
    }
}

// Sample y_der function
double y_der(double t, double y)
{
    return (t - y)/2;
}

int main()
{
    double a = 0, b = 3, t0 = 0, y0 = 1;

    euler(y_der, a, b, t0, y0, 1);
    euler(y_der, a, b, t0, y0, 0.5); // Do not use h = 1/2. Use 0.5 instead.
    euler(y_der, a, b, t0, y0, 0.25); 
    euler(y_der, a, b, t0, y0, 0.125);

    return 0;
}

