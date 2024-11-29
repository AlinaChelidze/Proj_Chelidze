"Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S"

def double_character(c, s):
    return s.replace(c, c * 2)


C = 'p'
S = 'python'
result = double_character(C, S)
print(result)