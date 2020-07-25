from typing import List

def lengthOfLastWord(s: str) -> int:
    splited_str = s.strip().split(" ")
    lst = list(splited_str)
    last_word = lst[len(lst)-1]
    length_of_last_word  = len(last_word)
    return length_of_last_word

assert lengthOfLastWord("Hello World") == 5
assert lengthOfLastWord("Hell") == 4
assert lengthOfLastWord("Hel l o") == 1
assert lengthOfLastWord("a") == 1
assert lengthOfLastWord("") == 0
assert lengthOfLastWord("a ") == 1
print("OK")