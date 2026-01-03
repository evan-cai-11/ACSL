def make_sin_triangle(width, M, N):
    M_row = -1
    M_col = -1
    N_row = -1
    N_col = -1
    row_size = width
    num = 1
    is_shrinking = True
    dir = 0
    i = 0

    while M_row == -1 or N_row == -1:
        if(dir == 0):
            for j in range(row_size):

                if(num == M):
                    M_row = i
                    M_col = j
                elif(num == N):
                    N_row = i
                    N_col = j
                
                num += 1

        else:
            for j in range(row_size - 1, -1, -1):

                if(num == M):
                    M_row = i
                    M_col = j
                elif(num == N):
                    N_row = i
                    N_col = j

                num += 1

        if(is_shrinking):
            row_size -= 1
            if(row_size == 1):
                is_shrinking = False
        else:
            row_size += 1
            if(row_size == width):
                is_shrinking = True

        dir = 1 - dir   
        i += 1

    return abs(M_row - N_row) + abs(M_col - N_col)

width, M, N = map(int, input().split())
distance = make_sin_triangle(width, M, N)
print(distance)