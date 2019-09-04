
from functools import reduce
from itertools import permutations
from typing import Mapping, Tuple, Iterator, List

notes = """CDECDCBA
GCDECDCB
ACDECDCB
ACDECBAG
FCDECBCD
CBCDECDC
BACBCDEF
CBCBCDEF
CDECBACB
ACDCDCBC
BCDECDCB
AGCBCDEC
BCDCDECB
ACDEFCBC
BACBCDEF
CBCDCBCB
ACBCDCBC
BCBAGFCB
AGCDCBAC
BCBCDCDC
BACDCDCD
CBCDCBCB"""


def value_convert(groups, value_map):
    values = []
    for g in groups:
        value_grouping = []
        for letter in g:
            value = value_map.get(letter)
            value_grouping.append(value)
        values.append(value_grouping)
    return values


def value_of_letters(permutation) -> Mapping:
    value_map = {}
    count = 0
    perm_list = list(permutation)
    for i in range(len(perm_list)):
        value_map[permutation[i]] = count
        count += 1
    return value_map


def group_sizer(arr, group_size):
    groupings = []
    for i in range(0, len(arr), group_size):
        groupings.append(arr[i:i + group_size])
    return groupings


def base_convert(base: int, grouping: List) -> int:
    count = len(grouping) - 1
    total = 0
    for num in grouping:
        total += base**count * num
        count -= 1
    return total


def value_convert(arr: List, value_map: Mapping) -> List[int]:
    values = []
    for a in arr:
        values.append(value_map.get(a))
    return values


def main():
    global notes
    notes_no_grouping = notes.replace("\n", "")
    notes_grouping = notes.split("\n")
    unique_letters = set(notes_no_grouping)
    perms = permutations(unique_letters)

    for perm in perms:
        values = value_convert(notes_no_grouping, value_of_letters(perm))
        groups = group_sizer(values, 3)
        converted_values = []
        for group in groups:
            converted_values.append(base_convert(7, group))
        url = ""
        for number in converted_values:
            url += str(chr(number))
        print(url)


if __name__ == "__main__":
    main()
