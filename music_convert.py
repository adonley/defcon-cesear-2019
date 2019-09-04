from typing import List

bin_str = """01110011 00111010 00101111 00101111
01100010 01101001 01110100 00101110
01101100 01111001 00101111 00110010
01011001 01000010 00110001 01011010
00110101 00110010"""

bin_list = []


def convert(l: List):
    string = ""
    for s in l:
        string += str(chr(int(s, 2)))
    return string


def main():
    global bin_list
    bins = bin_str.split()
    s = convert(bins)
    print(s)


if __name__ == "__main__":
    main()
