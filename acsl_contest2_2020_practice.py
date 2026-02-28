string = input()
string = string.replace(" ", "")

def is_number(character):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(string)):
        if(string[i] in digits):
            return True
    
    return False

def keep_alphanumeric(string):
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    result = ""

    for i in range(len(string)):
        if(is_number(string[i]) or string[i] in upper or string[i] in lower):
            result += string[i]

    return result

def count_occurrences(string):
    counts = {}
    for i in range(len(string)):
        if(string[i] not in counts):
            counts[string[i]] = 0
        counts[string[i]] += 1
    
    return counts

def sort(list):
    letters = [x for x in list if isinstance(x, str)]
    numbers = [x for x in list if isinstance(x, int)]

    letters.sort()
    numbers.sort()

    sorted_list = numbers + letters

    return sorted_list

def sort_reverse(list):
    letters = [x for x in list if isinstance(x, str)]
    numbers = [x for x in list if isinstance(x, int)]

    letters.sort(reverse=True)
    numbers.sort(reverse=True)

    sorted_list = letters + numbers

    return sorted_list

def sort_counts(counts):
    counts_arr = []
    keys_list = list(counts.keys())
    highest_count = counts[max(counts)]
    for i in range(highest_count):
        counts_arr.append([])
    for i in range(len(counts)):
        count = counts[keys_list[i]]
        counts_arr[count].append(keys_list[i])
        if(i % 2 == 0):
            counts_arr[count] = sort(counts_arr[count])
        else:
            counts_arr[count] = sort_reverse(counts_arr[count])
    for i in range(len(counts_arr)):
        if(len(counts_arr[i]) == 0):
            del counts_arr[i]

    return counts_arr

string = keep_alphanumeric(string)

counts = count_occurrences(string)

counts_arr = sort_counts(counts)

print(counts_arr)