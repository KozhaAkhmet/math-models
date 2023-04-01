from Trapezoidal import trapezoidal

def main():
    def polinomial(a, b, x):
        return (a*x + b*(1/x))**2

    solution = trapezoidal(polinomial, 1, 1, 1, 2, 2)
    print("Solution: " + str(solution))


if __name__ == '__main__':
    main()


"""
Output:
Boundaries: [1, 1.5, 2]
i:0 integral: 2.1736111111111107
i:1 integral: 4.909722222222221
Solution: 4.909722222222221
"""