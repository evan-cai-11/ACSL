def count_completed_tubes(tubes):
    return 0

def check_empty_tubes(tubes):
    return -1
    
def find_number_of_top_color(tube, color):
    count = 0
    for i in range(len(tube)):
        if(tube[i] != color):
            break
        else:
            count += 1

    return count

def top_color(tubes):
    color_counts = {}

    max_color_count = 0

    max_color = ""

    for i in range(len(tubes)):
        if(len(tubes[i]) > 0):
            color = tubes[i][0]
            color_counts[color] += 1
            if(color_counts[color] > max_color_count):
                max_color_count = color_counts[color]
                max_color = color
        
    return max_color

N = int(input())
tubes = input().split(" ")
tubes.append("")
tubes.append("")

print(tubes)

completed_tubes = count_completed_tubes(tubes)

failures_in_a_row = 0

moves = []

while(failures_in_a_row < N + 2 and completed_tubes < N):

    empty_tube = check_empty_tubes(tubes)

    # Check if there's an empty tube
    if(empty_tube != -1):

        # find the top color
        color = top_color(tubes)

        # For all tubes figure out whether the current tube needs moving and how many items need to be moved
        for i in range(len(tubes)):
            
            quantity = find_number_of_top_color(tubes[i], color)

            if(quantity > 0): # This means this tube needs moving
                # Actually move it
                tubes[empty_tube] = ("".join([color] * quantity)) + tubes[empty_tube]
                tubes[i] = tubes[i][quantity:]

                # Keep track of the move (for the problem)
                move = str(i + 1) + str(empty_tube + 1)
                moves.append(move)

    # After checking the rightmost tube, circulate back to check others to the left of the source tube until the marble has been moved.

    # If there are no empty tubes
        else:

            # look at the tubes from left to right starting with Tube #1.
            for source in range(N + 2):

                # Consider the tubes for the destination starting with the tube to the right of the source tube.
                for i in range(N + 1):
                    destination = 

                    # get the top of both the source tube and destination tubes
                    source_top_marble = tubes[source][0]
                    destination_top_marble = tubes[i][0]

                    # If possible, find the first tube where its top color can be moved to another tube. 
                    if(len(tubes[i]) < N and destination_top_marble == source_top_marble):
                        # enter means that there is a valid move
                        # reset failure count
                        failures_in_a_row = 0

                        # 
                        tubes[i].append(source_top_marble)
                        tubes[source][0] = ""

                    else:
                        # increase failure count
                        failures_in_a_row += 1

            
if(completed_tubes == N):
    print(moves, "WIN")
else:
    print(moves, "LOSE")