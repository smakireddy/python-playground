"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2
"""


def count_substring(st, sub_string):
    cnt = 0
    len_sub_str = len(sub_string)
    print(len(st))
    print(len_sub_str)
    print(len(st) - len_sub_str+1)
    for i in range(0, len(st) - len_sub_str+1):
        if sub_string == st[i:len_sub_str+i]:
            cnt += 1
    return cnt


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = "ABCDCDC"
    sub_string = "CDC"
    count = count_substring(string, sub_string)
    print(count)
