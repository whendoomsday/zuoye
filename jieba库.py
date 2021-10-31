import jieba
sentence=input()
words = jieba.lcut(sentence)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get('word', 0 )+ 1
items = list(counts.items())
print(items)

