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

# counting bigrams in a 2D torch tensor
import torch
N = torch.zeros((28,28), dtype=torch.int32)

chars = sorted(list(set(''.join(words))))
stoi = {s:i for i,s in enumerate(chars)}
stoi['<S>'] = 26
stoi['<E>'] = 27

for w in words:
  chs = ['<S>'] + list(w) + ['<E>']
  for ch1, ch2 in zip(chs, chs[1:]):
    ix1 = stoi[ch1]
    ix2 = stoi[ch2]
    N[ix1, ix2] += 1

itos = {i:s for s,i in stoi.items()}

# visualize the bigram
import matplotlib.pyplot as plt
# %matplotlib inline
plt.figure(figsize=(16,16))
plt.imshow(N, cmap='Reds')

for i in range(28):
  for j in range(28):
    chstr = itos[i] + itos[j]
    plt.text(j, i, chstr, ha='center', va='bottom', color='gray')
    plt.text(j, i, N[i, j].item(), ha='center', va='top', color='gray')
    
plt.axis('off')
plt.show()