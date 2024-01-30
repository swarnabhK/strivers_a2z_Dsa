# You are given a play list, where each song is represented by an integer. Your task to find out how long is the longest part of the play list that contains no song twice.
#[1,2,1,3,5,4,3,1], longest is [2,1,3,5,4]

l = [1,2,1,3,5,4,3,1]
left = 0
s = {l[0]}
find = ""
max_window = 0
for right in range(1,len(l)):
    if(l[right] in s):
        find = l[right]
    while(left<len(l) and l[left]!=find):
        left+=1
    if(left<len(l) and l[left]==find):
        s.remove(l[left])
        left+=1
    #now a valid window.
    s.add(l[right])
    max_window = max(max_window,right-left+1)

print(max_window)