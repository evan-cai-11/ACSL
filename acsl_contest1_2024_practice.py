def is_match(tile1, tile2):
    if(tile1[1] == tile2[0] or tile1[1] == tile2[1]):
        return True
    else:
        return False

def turn(top_nums, hand, draw_pile):
    for i in range(4):
        for j in range(len(hand)):
            if(is_match(top_nums[i], hand[j])):
                hand.remove(hand[j])
                top_nums[i] = hand[j][]



start_nums = input().split()
hand = input().split(" ")
draw_pile = input().split(" ")