def inward(row, col, target):
    x = 0
    y = 0
    target_x = 0
    target_y = 0

    direction_vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    array = [[0 for _ in range(col)] for _ in range(row)]
    lim = row * col

    curr_dir = 0

    for i in range(1, lim + 1):
        array[y][x] = i
        if(i == target):
            print("enter")
            target_x = x
            target_y = y

        next_x = x + direction_vectors[curr_dir][0]
        next_y = y + direction_vectors[curr_dir][1]

        if (next_x >= 0 and next_x < col and next_y >= 0 and next_y < row and array[next_y][next_x] == 0):
            x = next_x
            y = next_y
        else:   
            curr_dir = (curr_dir + 1) % 4 
            x += direction_vectors[curr_dir][0]
            y += direction_vectors[curr_dir][1]

    for row_stuff in array:
        print(row_stuff)

    return target_x, target_y

def setup():
    row, col = input().split()
    in_out = input()
    target = input()
    row_ans, col_ans = inward(int(row), int(col), int(target))
    print(row_ans, col_ans)

setup()