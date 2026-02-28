guess1, dist_value1 = input().split()
guess2, dist_value2 = input().split()
guess3, dist_value3 = input().split()

def find_destinations(guess, dist_value):
    guess_row = int(guess[:2], 16)
    guess_col = int(guess[2:], 16)
    dist1 = int(dist_value[:2], 16)
    dist2 = int(dist_value[2:], 16)
    
    destinations = []

    left1 = guess_row - dist1
    left2 = guess_row - dist2
    up1 = guess_col - dist2
    up2 = guess_col - dist1
    right1 = guess_row + dist1
    right2 = guess_row + dist2
    down1 = guess_col + dist2
    down2 = guess_col + dist1

    if(left1 >= 0 and up1 >= 0):
        leftup1 = (left1, up1)
        destinations.append(leftup1)
    if(left1 >= 0 and down1 <= 256):
        leftdown1 = (left1, down1)
        destinations.append(leftdown1)
    if(right1 <= 256 and up1 >= 0):
        rightup1 = (right1, up1)
        destinations.append(rightup1)
    if(right1 <= 256 and down1 <= 256):
        rightdown1 = (right1, down1)
        destinations.append(rightdown1)
    if(left2 >= 0 and up2 >= 0):
        leftup2 = (left2, up2)
        destinations.append(leftup2)
    if(left2 >= 0 and down2 <= 256):
        leftdown2 = (left2, down2)
        destinations.append(leftdown2)
    if(right2 <= 256 and up2 >= 0):
        rightup2 = (right2, up2)
        destinations.append(rightup2)
    if(right2 <= 256 and down2 <= 256):
        rightdown2 = (right2, down2)
        destinations.append(rightdown2)

    return destinations

destinations1 = find_destinations(guess1, dist_value1)
destinations2 = find_destinations(guess2, dist_value2)
destinations3 = find_destinations(guess3, dist_value3)
destinations = destinations1 + destinations2 + destinations3

def find_destination(destinations):
    for i in range(len(destinations)):
        if(destinations.count(destinations[i]) == 3):
            destination = destinations[i]

    return destination


destination = find_destination(destinations)

x = ""
y = ""

if(len(hex(destination[0])[2:]) == 1):
    x = "0" + hex(destination[0])[2:].upper()
else:
    x = hex(destination[0])[2:].upper()

if(len(hex(destination[1])[2:]) == 1):
    y = "0" + hex(destination[1])[2:].upper()
else:
    y = hex(destination[1])[2:].upper()

destination = (x, y)

print("(" + destination[0] + "," + destination[1] + ")")