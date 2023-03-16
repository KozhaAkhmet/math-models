#include "Euler.h"

int main()
{
    double a = 0, b = 3, t0 = 0, y0 = 1;

    euler(y_der, a, b, t0, y0, 1);
    euler(y_der, a, b, t0, y0, 0.5); // Do not use h = 1/2. Use 0.5 instead.
    euler(y_der, a, b, t0, y0, 0.25); 
    euler(y_der, a, b, t0, y0, 0.125);

    return 0;
}

// Run in terminal:
// $ g++ g++ Euler.cpp main.cpp -o output
//
// then execute it:
// $ ./output

/*
Output:
H is: 1
0 0.5
1 0.75
2 1.375

H is: 0.5
0 0.75
1 0.8125
2 1.10938
3 1.58203
4 2.18652
5 2.88989

H is: 0.25
0 0.875
1 0.890625
2 1.0293
3 1.27563
4 1.61618
5 2.03916
6 2.53426
7 3.09248
8 3.70592
9 4.36768
10 5.07172
11 5.81276

H is: 0.125
0 0.9375
1 0.941406
2 1.00757
3 1.1321
4 1.31134
5 1.54188
6 1.82051
7 2.14423
8 2.51022
9 2.91583
10 3.35859
11 3.83618
12 4.34642
13 4.88726
14 5.45681
15 6.05326
16 6.67493
17 7.32025
18 7.98773
19 8.676
20 9.38375
21 10.1098
22 10.8529
23 11.6121

*/