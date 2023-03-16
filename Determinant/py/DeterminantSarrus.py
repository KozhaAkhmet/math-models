def determinant_sarrus(A: list):
    if(len(A) == 3):
        buffer = [A[0],A[1],A[2],A[0],A[1]] # Copying first two rows 
        to_right = 0.0
        to_left = 0.0
        for i in range(3):
               to_right += buffer[i][0] * buffer[i + 1][1] * buffer[i + 2][2]
               to_left += buffer[i][2] * buffer[i + 1][1] * buffer[i + 2][0]

        print("Determinant with sarrus is: " + str(to_right - to_left))
        return to_right - to_left
    else:
        print("Not compatible dimention for Sarrus!")
        return None

