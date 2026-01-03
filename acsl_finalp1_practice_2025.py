def inward(row, col, target):
    x = 0
    y = 0
    target_x = 0
    target_y = 0
    curr_dir = 1
    array = [[0 for _ in range(col)] for _ in range(row)]
    lim = row * col
    for i in range(1, lim + 1):
        array[y][x] = i
        if(i == target):
            print("enter")
            target_x = x
            target_y = y
        
        if(curr_dir == 1):
            if(x + 1 < col and array[y][x + 1] == 0):
                x += 1
            else:
                curr_dir = (curr_dir + 1) % 4 
                y += 1
        elif(curr_dir == 2):
            if(y + 1 < row and array[y + 1][x] == 0):
                y += 1
            else:
                curr_dir = (curr_dir + 1) % 4 
                x -= 1
        elif(curr_dir == 3):
            if(x - 1 >= 0 and array[y][x - 1] == 0):
                x -= 1
            else:
                curr_dir = (curr_dir + 1) % 4 
                y -= 1
        else:
            if(y - 1 >= 0 and array[y - 1][x] == 0):
                y -= 1
            else:
                curr_dir = (curr_dir + 1) % 4 
                x += 1

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