import math

rows = 8
columns = 5
tiles = [
    [4, 128, 4, 128, 32], 
    [16, 16, 4, 256, 16], 
    [32, 4, 16, 64, 4], 
    [8, 64, 64, 256, 8], 
    [16, 2, 2, 256, 4], 
    [32, 128, 2, 64, 8], 
    [256, 32, 128, 16, 2], 
    [8, 32, 32, 4, 32]
]
path = "0"

def remove_longest_path(path, tiles):
    sum = 0
    new_path = path.split("-")
    for i in range(len(new_path)):
        row = int(new_path[i][0])
        column = int(new_path[i][1])
        sum += tiles[row - 1][column - 1]
        tiles[row - 1][column - 1] = 0
        
    return sum

def edit_last_tile(tiles, sum):
    new_path = path.split("-")
    last_tile_row = int(new_path[len(new_path) - 1][0])
    last_tile_column = int(new_path[len(new_path) - 1][1])
    i = 1
    while True:
        if((2 ** i) > sum):
            tiles[last_tile_row - 1][last_tile_column - 1] = 2 ** i
            break
        else:
            i += 1

def remove_tiles(tiles):
    low, high = get_power_of_2(tiles)
    for i in range(rows):
        for j in range(columns):
            if(tiles[i][j] < low):
                tiles[i][j] = 0

    return high

def get_power_of_2(tiles):
    highest_power_of_2 = 2
    for i in range(rows):
        for j in range(columns):
            if(tiles[i][j] > highest_power_of_2):
                highest_power_of_2 = tiles[i][j]

    lowest_possible_power_of_2 = highest_power_of_2 / (2 ** 7)

    return lowest_possible_power_of_2, highest_power_of_2
    
def shift_down(tiles):
    rows = len(tiles)
    if (rows == 0):
        return
    columns = len(tiles[0])

    for i in range(columns):
        bottom = rows - 1
        for j in range(rows - 1, -1, -1):
            if(tiles[j][i] != 0):
                if(bottom != j):
                    tiles[bottom][i] = tiles[j][i]
                    tiles[j][i] = 0
                bottom -= 1

def fill_empty_tiles(tiles, highest_power_of_2):
    high_power = math.log(highest_power_of_2, 2)
    curr_power = high_power
    for i in range(rows):
        for j in range(columns):
            if(tiles[i][j] == 0):
                tiles[i][j] = 2 ** curr_power
                if(curr_power - 1 >= (high_power - 7) and curr_power - 1 > 0):
                    curr_power -= 1
                else:
                    curr_power = high_power

sum = remove_longest_path(path, tiles)
edit_last_tile(tiles, sum)
highest_power_of_2 = remove_tiles(tiles)
shift_down(tiles)
fill_empty_tiles(tiles, highest_power_of_2)
print(tiles)