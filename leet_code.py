# Online Compiler 1: https://www.onlinegdb.com/online_python_compiler (logged in with google) has debug option
# Online Compiler 2: https://replit.com/@orenbezalely  (logged in with google)
# Online Compiler 2: https://www.programiz.com/online-compiler

from typing import List



def longest_common_prefix(v: List[str]) -> str:
    """takes a list of strings and returns the longest common prefix that is shared among all the strings"""
    # O(n * m)
    number_of_words = len(v)
    shortest_word = min([len(word) for word in v])
    longest_prefix = ''

    for i in range(shortest_word):

        # character of first word
        first_word_char = v[0][i]

        # do chars of subsequent words match the first char? Genterate Bool list.
        char_list = [v[j][i] == first_word_char for j in range(1, number_of_words)]

        if all(char_list):
            longest_prefix += first_word_char
        else:
            break
    return longest_prefix


# O(m)
def longest_common_prefix_optimal(v: List[str]) -> str:
    """takes a list of strings and returns the longest common prefix that is shared among all the strings"""

    number_of_words = len(v)
    shortest_word = min([len(word) for word in v])
    longest_prefix = ''
    v = sorted(v)  # now we will only need to compare the first and last entries

    first = v[0]
    last = v[-1]

    for i in range(min(len(first), len(last))):

        if first[i] == last[i]:
            longest_prefix += first[i]
        else:
            break
    return longest_prefix

def is_palindrome(s: str) -> bool:
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]


def valid_palindrome(s: str) -> bool:
    def is_palindrome_range(i: int, j: int) -> bool:
        # Helper function to check if substring s[i:j+1] is a palindrome
        return all(s[k] == s[j - k + i] for k in range(i, j))

    # Two pointers approach
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1

    return True  # String is already a palindrome

if __name__ == '__main__':
    print(valid_palindrome("abca"))  # True
    print(valid_palindrome("racecar"))  # True
    print(valid_palindrome("abc"))  # False
    # assert longest_common_prefix(["flower", "flow", "flight"]) == 'fl'
    # assert longest_common_prefix(["red", "rabbit", "rod", "ride"]) == 'r'
    # assert longest_common_prefix(["dog", "racecar", "car"]) == ''
    # assert longest_common_prefix(['']) == ''
    # print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    # print(is_palindrome("racecar"))  # True
    # print(is_palindrome("hello"))  # False
