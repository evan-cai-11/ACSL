def check_arrays(left_array, right_array, internal_depths):
    left_count = 0
    right_count = 0
    leaf_count = 0
    sum_internal_depths = 0
    sum_external_depths = 0

    for i in range(len(left_array)):
        if(left_array[i] != -1 and right_array[i] == -1):
            left_count += 1
            sum_external_depths += (internal_depths[i] + 1)
        elif(left_array[i] == -1 and right_array[i] != -1):
            right_count += 1
            sum_external_depths += (internal_depths[i] + 1)
        elif(left_array[i] == -1 and right_array[i] == -1):
            leaf_count += 1
            sum_external_depths += 2 * (internal_depths[i] + 1)
            print(sum_external_depths)

        sum_internal_depths += internal_depths[i]
    
    return left_count, right_count, leaf_count, sum_internal_depths, sum_external_depths

def tree(word):
    left_array = [-1 for _ in range(len(word))]
    right_array = [-1 for _ in range(len(word))]
    internal_depths = [0 for _ in range(len(word))]
    answers = []

    for i in range(1, len(word)):
        next = 0
        while True:
            if(word[i] <= word[next]):
                if(left_array[next] == -1):
                    left_array[next] = i
                    internal_depths[i] += 1
                    break
                else:
                    next = left_array[next]
                    internal_depths[i] += 1
            else:
                if(right_array[next] == -1):
                    right_array[next] = i
                    internal_depths[i] += 1
                    break
                else:
                    next = right_array[next]
                    internal_depths[i] += 1

    answers = check_arrays(left_array, right_array, internal_depths)

    return answers

word = input()
answers = tree(word)
print(answers)