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
  chs = ['.'] + list(w) + ['.']
  for ch1, ch2 in zip(chs, chs[1:]):
    bigram = (ch1, ch2)
    c[bigram] = c.get(bigram, 0) + 1

# sorting the key value
sorted(c.items(), key = lambda kv: -kv[1])

# counting bigrams in a 2D torch tensor
import torch
N = torch.zeros((27,27), dtype=torch.int32)

chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}

for w in words:
  chs = ['.'] + list(w) + ['.']
  for ch1, ch2 in zip(chs, chs[1:]):
    ix1 = stoi[ch1]
    ix2 = stoi[ch2]
    N[ix1, ix2] += 1

# Commented out IPython magic to ensure Python compatibility.
# visualize the bigram
import matplotlib.pyplot as plt
# %matplotlib inline
plt.figure(figsize=(16,16))
plt.imshow(N, cmap='Reds')

for i in range(27):
  for j in range(27):
    chstr = itos[i] + itos[j]
    plt.text(j, i, chstr, ha='center', va='bottom', color='gray')
    plt.text(j, i, N[i, j].item(), ha='center', va='top', color='gray')
plt.axis('off')
plt.show()

# sampling the first character of the word
N[0]

# convert to probability distribution
p = N[0].float() # to normalize the count
p = p / p.sum()
p

g = torch.Generator().manual_seed(2147483647)
ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
print(itos[ix])

# sample from distribution
g = torch.Generator().manual_seed(2147483647)
p = torch.rand(3, generator=g)
p = p / p.sum()
print(p)

torch.multinomial(p, num_samples=20, replacement=True, generator=g)