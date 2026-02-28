import string

def is_valid(plate):
    if(plate[0] in string.ascii_uppercase and plate[1] in string.ascii_uppercase and plate[2] in string.ascii_uppercase and plate[3] in string.digits and plate[4] in string.digits and plate[5] in string.digits and plate[6] in string.digits):
        return True
    else:
        return False

def alphabet_half(plate):
    alphabet_beginning_half = string.ascii_uppercase[:13]
    alphabet_end_half = string.ascii_uppercase[-13:]
    if(plate[0] in alphabet_beginning_half and plate[1] in alphabet_beginning_half and plate[2] in alphabet_beginning_half):
        return "B"
    if(plate[0] in alphabet_end_half and plate[1] in alphabet_end_half and plate[2] in alphabet_end_half):
        return "E"
    
    return ""

def is_consecutive(plate):
    values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    if((values[plate[0]] == values[plate[1]] - 1 and values[plate[1]] == values[plate[2]] - 1) == True and ((int(plate[3]) == int(plate[4]) - 1 and int(plate[4]) == int(plate[5]) - 1 and int(plate[5]) == int(plate[6]) - 1) == False and (int(plate[3]) == int(plate[4]) + 1 and int(plate[4]) == int(plate[5]) + 1 and int(plate[5]) == int(plate[6]) + 1) == False)):
        return "I"
    if((values[plate[0]] == values[plate[1]] + 1 and values[plate[1]] == values[plate[2]] + 1) == True and ((int(plate[3]) == int(plate[4]) - 1 and int(plate[4]) == int(plate[5]) - 1 and int(plate[5]) == int(plate[6]) - 1) == False and (int(plate[3]) == int(plate[4]) + 1 and int(plate[4]) == int(plate[5]) + 1 and int(plate[5]) == int(plate[6]) + 1) == False)):
        return "D"
    if(((values[plate[0]] == values[plate[1]] - 1 and values[plate[1]] == values[plate[2]] - 1) == False and (values[plate[0]] == values[plate[1]] + 1 and values[plate[1]] == values[plate[2]] + 1) == False) and (int(plate[3]) == int(plate[4]) - 1 and int(plate[4]) == int(plate[5]) - 1 and int(plate[5]) == int(plate[6]) - 1)):
        return "I"
    if(((values[plate[0]] == values[plate[1]] - 1 and values[plate[1]] == values[plate[2]] - 1) == False and (values[plate[0]] == values[plate[1]] + 1 and values[plate[1]] == values[plate[2]] + 1) == False) and (int(plate[3]) == int(plate[4]) + 1 and int(plate[4]) == int(plate[5]) + 1 and int(plate[5]) == int(plate[6]) + 1)):
        return "D"
    
    return ""
    
def is_hex(plate):
    if(plate[0] in string.hexdigits and plate[1] in string.hexdigits and plate[2] in string.hexdigits):
        return "H"
    
    return ""
    
def is_octal(plate):
    if(int(plate[3]) != 0 and plate[3] in string.octdigits and plate[4] in string.octdigits and plate[5] in string.octdigits and plate[6] in string.octdigits):
        return "O"
    
    return ""
    
def is_palindrome(plate):
    letters = plate[:3]
    digits = plate[-4:]
    if(letters == letters[::-1] or digits == digits[::-1]):
        return "P"
    
    return ""
    
def contains_repeats(plate):
    letters = plate[:3]
    digits = plate[-4:]
    for i in range(3):
        if(letters[i] in letters.replace(letters[i], "", 1)):
            return "R"
    
    for i in range(4):
        if(digits[i] in digits.replace(digits[i], "", 1)):
            return "R"
        
    return ""
        
def num_equals_sum(plate):
    digits = plate[-4:]
    for i in range(4):
        str = digits.replace(digits[i], "", 1)
        sum = 0
        for j in range(3):
            sum += int(str[j])
        if(int(digits[i]) == sum):
            return "S"
        
    return ""
        
def make_output_string(plate):
    output_string = ""
    output_string += alphabet_half(plate)
    output_string += is_consecutive(plate)
    output_string += is_hex(plate)
    output_string += is_octal(plate)
    output_string += is_palindrome(plate)
    output_string += contains_repeats(plate)
    output_string += num_equals_sum(plate)
    output_string = sorted(output_string)
    answer_string = ""
    for i in range(len(output_string)):
        answer_string += output_string[i]
    return answer_string

plate = input()
if(is_valid(plate) == False):
    quit()

output_string = make_output_string(plate)
print(output_string)