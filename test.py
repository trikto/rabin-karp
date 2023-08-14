#21001512 - SCS2201 Data Structures and Algorithms III - Assignment 01


#RABIN KARP

# computing hash value
def hash_func(pattern):
    hash = 0
    power = 0

    rev_pattern = pattern[::-1]

    for value in rev_pattern:
        hash += (127 ** power) * ord(value)
        power += 1

    return hash

#sliding function
def sliding_func(pattern, string):
    arr = []
    pattern_hash = hash_func(pattern)
    pattern_length = len(pattern)
    string_length = len(string)

    for i in range(string_length - pattern_length + 1):
        substring = string[i:i+pattern_length]
        if (pattern_hash == hash_func(substring)):
            if pattern == substring:
                arr.append(i)
    return arr

pattern = input("Enter the pattern: ")
string = input("Enter the string: ")

#For | 
if "|" in pattern:
    patterns = pattern.split("|")

    dictionary = {}
    for pattern in patterns:
        dictionary[pattern] = sliding_func(pattern, string)
    print(dictionary)

# For \b (word boundaries)
elif (pattern[:2] == "\\b") and (pattern[-2:] == "\\b"):
    print(sliding_func(pattern[2:-2], string))

#For ^
elif (pattern[0] == "^"):
    matching_list = sliding_func(pattern[1:], string)
    if 0 in matching_list:
        print(True)
    else:
        print(False)

#For $
elif (pattern[-1] == "$"):
    matching_list = sliding_func(pattern[0:-1], string)
    if (len(string) - len(pattern[:-1])) in matching_list:
        print(True)
    else:
        print(False)