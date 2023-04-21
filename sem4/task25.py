
sequence = 'a a b b c c' 
result = ''
for i in range(len(sequence)):
    if sequence[0:i:].count(sequence[i]) == 0:
        result += sequence[i]
    else:
        result += f'{sequence[i]}_{sequence[0:i].count(sequence[i])}'
print(sequence[0:i], result)
print(result)