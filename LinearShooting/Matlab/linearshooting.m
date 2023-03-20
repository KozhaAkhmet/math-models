% From lesson: Partial Differetial Eq. with Numerical Mehods 
% Solving Linear shooting problem with Runge Kutta 

function[  w, u1, u2, v1, v2, yA, AbsErr] = linearshooting(a,b,alpha,beta, N)

p = @(x) -2./x;
q = @(x) 2./(x.^2);
r = @(x) sin(log(x)) / (x.^2);

% Step size for Runge Kutta

h = (b-a) / N;

x = a:h:b;

% First IVP

u1(1) = alpha;
u2(1) = 0;

% Second IVP

v1(1) = 0;
v2(1) = 1;

for i  = 1:N
    k1  = h*u2(i);
    m1 = h*(p(x(i))*u2(i) + q(x(i))* u1(i) + r(x(i)));
    k2 = h*(u2(i) + m1/2);
    m2 = h*(p(x(i) + h/2) * (u2(i) + m1/2) + q(x(i) + h/2) * (u1(i) + k1/2) + r(x(i) + h/2));
    k3 = h*(u2(i) + m2/2);
    m3 = h*(p(x(i) + h/2) * (u2(i) + m2/2) + q(x(i) + h/2) * (u1(i) + k2/2) + r(x(i) + h/2));
    k4 = h*(u2(i) + m3);
    m4 = h*(p(x(i) + h) * (u2(i) + m3) + q(x(i) + h) * (u1(i) + k3) + r(x(i) + h));

    u1(i+1) = u1(i) + (1/6) * (k1 + 2*k2 + 2*k3 + k4 );
    u2(i+1) = u2(i) + (1/6) * (m1 + 2*m2 + 2*m3 + m4);

    
    t1  = h * v2(i);
    s1  = h*(p(x(i)) * v2(i) + q(x(i))  * v1(i));
    t2 = h* (v2(i) + s1/2);
    s2 = h*(p(x(i) + h/2) * (v2(i) + s1/2) + q(x(i) + h/2) * (v1(i) + t1/2));
    t3 = h * (v2(i) + s2/2);
    s3 = h*(p(x(i) + h/2) * (v2(i) + s2/2) + q(x(i) + h/2) * (v1(i) + t2/2));
    t4 = h* (v2(i) + s3);
    s4 = h*(p(x(i) + h/2) * (v2(i) + s3) + q(x(i) + h/2) * (v1(i) + t3));

    v1(i+1) = v1(i) + (1/6) * (t1 + 2*t2 + 2*t3 + t4); % y2
    v2(i+1) = v2(i) + (1/6) * (s1 + 2*s2 + 2*s3 + s4); % y2'

end

for  i = 1:N+1
    w(i) = u1(i) + ((beta - u1(end)) / (v1(end))) * v1(i);
end

% Analytical Solution

c2 = (1/70) * (8 - 12*sin(log(2)) - 4*cos(log(2)));
c1 = (11/10) - c2;
yA = c1*x + c2./x.^2 - (3/10) * sin(log(x)) - (1/10) * cos(log(x));

% Absolute error

AbsErr = abs(yA - w);