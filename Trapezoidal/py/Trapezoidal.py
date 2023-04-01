

def arrange(x0, x1, n):
    list = [x0]

    for i in range(1, n):
        list.append(list[i-1] + i*(x1-x0)/n)

    list.append(x1)
    return list


def trapezoidal(func, a, b, x0, x1, n=100):
    integral = 0
    values = arrange(x0, x1, n)
    print("Boundaries: " + str(values))
    for i in range(0, len(values)-1):
        
        integral += (values[i+1] - values[i]) * (func(a, b, values[i+1]) + func(a, b, values[i]))/2
        print("i:" + str(i) + " integral: " + str(integral))
    return integral


