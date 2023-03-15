def determinant_sarrus(A: list):
    if(len(A) == 3):
        buffer = [A[0],A[1],A[2],A[0],A[1]]
        to_right = 0.0
        to_left = 0.0
        for i in range(3):
               to_right += buffer[i][0] * buffer[i + 1][1] * buffer[i + 2][2]
               to_left += buffer[i][2] * buffer[i + 1][1] * buffer[i + 2][0]

        print("Determinant with sarrus is: " + str(to_right - to_left))
        return to_right - to_left
    else:
        return None

    
def main():
    A = [[1,5,3],[1,2,7],[9,2,3]]
    determinant_sarrus(A)

if __name__ == '__main__':
   main()