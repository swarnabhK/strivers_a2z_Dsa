from collections import defaultdict
def frequencySort(s):
    counts = defaultdict(int)
    for c in s:
        if c not in counts:
            counts[c] = [c,1]
        else:
            counts[c][1]+=1
    l = sorted(counts.values(),key= lambda x:x[1],reverse = True)
    return "".join(c[0]*c[1] for c in l)


print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))