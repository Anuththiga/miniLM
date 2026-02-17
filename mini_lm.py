# -*- coding: utf-8 -*-

# read the dataset
words = open('anime_names.txt', 'r').read().splitlines()

print(words[:20])

print(len(words))

# longest word
print(max(len(w) for w in words))

# shortes word
print(min(len(w) for w in words))

for w in words[:2]:
  for ch1, ch2 in zip(w, w[1:]):
    print(ch1, ch2)