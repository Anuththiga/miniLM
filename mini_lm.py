# -*- coding: utf-8 -*-

# read the dataset
words = open('anime_names.txt', 'r').read().splitlines()

print(words[:20])

print(len(words))

# longest word
print(max(len(w) for w in words))

# shortes word
print(min(len(w) for w in words))

# bigram implementation
c = {}
for w in words:
  chs = ['<S>'] + list(w) + ['<E>']
  for ch1, ch2 in zip(chs, chs[1:]):
    bigram = (ch1, ch2)
    c[bigram] = c.get(bigram, 0) + 1

# sorting the key value
sorted(c.items(), key = lambda kv: -kv[1])