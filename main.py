from functools import reduce
from itertools import permutations
from typing import Mapping, Tuple, Iterator, List
import csv

table = {
    0: '+',
    1: '-',
    2: '0',
    3: '1',
    4: '2',
    5: '3',
    6: '4',
    7: '5',
    8: '6',
    9: '7',
    10: '8',
    11: '9',
    12: 'A',
    13: 'B',
    14: 'C',
    15: 'D',
    16: 'E',
    17: 'F',
    18: 'G',
    19: 'H',
    20: 'I',
    21: 'J',
    22: 'K',
    23: 'L',
    24: 'M',
    25: 'N',
    26: 'O',
    27: 'P',
    28: 'Q',
    29: 'R',
    30: 'S',
    31: 'T',
    32: 'U',
    33: 'V',
    34: 'W',
    35: 'X',
    36: 'Y',
    37: 'Z',
    38: 'a',
    39: 'b',
    40: 'c',
    41: 'd',
    42: 'e',
    43: 'f',
    44: 'g',
    45: 'h',
    46: 'i',
    47: 'j',
    48: 'k',
    49: 'l',
    50: 'm',
    51: 'n',
    52: 'o',
    53: 'p',
    54: 'q',
    55: 'r',
    56: 's',
    57: 't',
    58: 'u',
    59: 'v',
    60: 'w',
    61: 'x',
    62: 'y',
    63: 'z'
}


def read_csv():
    c = []
    first = True
    with open('./caesar.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if first:
                first = False
            else:
                c.append(row[:len(row) - 1])
    return c


def rotate_left(c):
    transformation = []
    # Initialize the arrays of colors within the transformation
    for i in range(0, len(c[0])):
        transformation.append([])
    # Populate with new values
    for i in range(len(c[0]) - 1, -1, -1):
        for j in range(0, len(c)):
            transformation[len(c[0]) - i - 1].append(c[j][i])
    return transformation


def representations(list_of_lists) -> Iterator[Tuple]:
    unique_letters = set(reduce(list.__add__, list_of_lists))
    return permutations(unique_letters)


def value_of_letters(permutation) -> Mapping:
    value_map = {}
    count = 0
    perm_list = list(permutation)
    for i in range(len(perm_list)):
        value_map[permutation[i]] = count
        count += 1
    return value_map


def groups_of(list_of_letters):
    groupings = []
    grouping_size = 3
    for i in range(0, len(list_of_letters), grouping_size):
        groupings.append(list_of_letters[i:i+grouping_size])
    return groupings


def base6_grouping_to_base2(grouping):
    count = len(grouping) - 1
    total = 0
    for num in grouping:
        total += 6**count * num
        count -= 1
    return total


def base6_to_base2(num):
    base10_from_base6 = int(str(num), 6)
    return str("{0:#b}".format(base10_from_base6)[2:])


def value_convert(groups, value_map):
    values = []
    for g in groups:
        value_grouping = []
        for letter in g:
            value = value_map.get(letter)
            value_grouping.append(value)
        values.append(value_grouping)
    return values


def anscii_representation():
    pass


def main():
    c = read_csv()
    # just the variant blocks
    enc = c[3:len(c)-3]
    encodings = [enc]
    encoding1 = rotate_left(enc)
    encoding2 = rotate_left(encoding1)
    encoding3 = rotate_left(encoding2)
    encodings.append(encoding1)
    encodings.append(encoding2)
    encodings.append(encoding3)
    representations(enc)
    # Total permutations of the letters
    reps = representations(enc)
    t = []
    for encoding in encodings:
        flattened = reduce(list.__add__, encoding)
        for representation in reps:
            rep_value = value_of_letters(representation)
            three = groups_of(flattened)
            values_base6 = value_convert(three, rep_value)
            str_base2_values = []
            for numbers in values_base6:
                # grouped_values = ""
                # for n in numbers:
                #     grouped_values += base6_to_base2(n)
                # str_base2_values.append(grouped_values)
                binary_rep = base6_grouping_to_base2(numbers)
                str_base2_values.append(binary_rep)
            #
            url = ""
            for number in str_base2_values:
                url += str(chr(number))
            t.append(url)
    with open("ouput.txt", 'w') as f:
        for u in t:
            # Make sure it's within the anscii table we're interested in
            if not all(32 < e < 177 for e in u):
                continue
            f.write(u)
            f.write("\n")


if __name__ == "__main__":
    main()
