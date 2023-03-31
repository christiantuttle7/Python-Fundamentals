    # find the histogram (frequency of each unique character) in a word
def histogram(word, hist):
    for c in word:
        c = c.lower()
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1

h = {}
histogram('Mississippim', h)
print(h.items())
for k, v in h.items():
    print(k, v)