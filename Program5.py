filename= open("ballot.txt")
contents=filename.read()
arr=contents.split("\n")
abc_arr=[[],[],[]]

win_msg_prepend="     "
true_win_msg=win_msg_prepend

for i in arr:
    if i!="":
        temp= i.split(" ")
        for j in range(len(temp)):
            abc_arr[j].append(temp[j])

vote_count={
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0
}

voter_count=0
for i in abc_arr[0]: #1st choice
    if i in vote_count:
        vote_count[i]+=1
    voter_count+=1
win=voter_count/2
cand=vote_count.keys()
for i in cand:
    if vote_count[i]>win:
        true_win_msg+=i+" wins"

for i in abc_arr[1]:  #2nd choice
    if i in vote_count:
        vote_count[i]+=1
    

win_arr=[]
win2=""
for i in cand:
    if vote_count[i]>win:
        win_arr.append([i, vote_count[i]])
        temp_max=0
        for i in win_arr:
            if i[1]>temp_max:
                temp_max=i
                win2=i[0]
        if true_win_msg==win_msg_prepend:
            true_win_msg+=win2+" wins"

        
for i in abc_arr[2]:  #3rd choice
    if i in vote_count:
        vote_count[i]+=1
temp_max=0
win3 = max(vote_count, key= lambda x: vote_count[x])
if true_win_msg==win_msg_prepend:
    true_win_msg=win_msg_prepend+win3+" wins"
for i in vote_count.keys():
    if vote_count[win3]==vote_count[i] and win3!=i:
        true_win_msg="tie"

if true_win_msg==win_msg_prepend:
    true_win_msg="tie"
print(true_win_msg)