"""
Дана строка, состоящая из русских слов, разделенных пробелами (одним или
несколькими). Найти количество слов в строке.
"""

def count_words(s):
    words = list(filter(bool, s.split()))
    return len(words)

input_string = "В этой строке пять слов"
word_count = count_words(input_string)
print(word_count)
