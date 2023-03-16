#ifndef EULER_H
#define EULER_H

double y_der(double t, double y);
void euler(double (*y_der)(double, double), double a, double b, double t0, double y0, double h);


#endif // EULER_H