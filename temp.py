from typing import List

def longest_common_prefix_3(v: List[str]) -> str:
    ans = ""
    v = sorted(v)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans

def longest_common_prefix_2(strs: List[str]) -> str:
    if strs == None or len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]


def longest_common_prefix(str_list: List[str]) -> str:
    number_of_words = len(str_list)
    smallest_word = min([len(word) for word in str_list])
    longest_prefix = ''

    for i in range(smallest_word):
        first_char = str_list[0][i]  # character of first word
        char_list = [str_list[j][i] == first_char for j in range(1, number_of_words)]
        if all(char_list):
            longest_prefix += first_char
        else:
            break
    return longest_prefix


if __name__ == '__main__':

    assert longest_common_prefix_3(["flower", "flow", "flight"]) == 'fl'
    assert longest_common_prefix_3(["flower", "floored", "flog", "flow"]) == 'flo'
    assert longest_common_prefix_3(["dog", "racecar", "car"]) == ''
