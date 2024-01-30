# You are given a list containing 
# n integers. How many ways can we choose a sublist that contains exactly two distinct integers?
# [1,2,3,3,2,2,4,2] has 14 such sublists.

l = [1, 2, 3, 3, 2, 2, 4, 2]
count = 0

for i in range(len(l)):
    s = set()
    s.add(l[i])
    for j in range(i + 1, len(l)):
        s.add(l[j])
        if len(s) == 2:
            count+=1
        elif(len(s)>2):
            break

print(count)

        