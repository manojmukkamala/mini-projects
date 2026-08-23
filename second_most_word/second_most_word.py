s = "This is an example paragraph. The goal of this program is to find the second most repeated word in this paragraph. If there is more than one word then print them all."

tokens = s.split()

punc = '.,'

cleaned_tokens = [t.translate(str.maketrans('', '', punc)) for t in tokens]

ctr = {}

for t in cleaned_tokens:
    ctr[t] = 1 + ctr.get(t, 0)

second_highest = sorted(list(set(ctr.values())))[-2]

print({k: v for k, v in ctr.items() if v == second_highest}.keys())