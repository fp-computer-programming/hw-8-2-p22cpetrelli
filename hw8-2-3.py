# Author: CJP 12/09/21
def three_letter_words(lst):
    letter = 0
    for num in lst:
        if len(num) == 3:
            letter += 1
            return letter


three_letter_words(["cat", "bat", "apple"]) == 2
three_letter_words(["apple", "hippo", "mouse"]) == 0
three_letter_words(["hop", "pop", "bop"]) == 3