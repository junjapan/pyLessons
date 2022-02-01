import random

allMem=['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']

print(len(allMem))
print(allMem)
random.shuffle(allMem)
print(allMem)

teamNum=2
memNum=int(len(allMem)/teamNum)
s='A'

for i in range(0,teamNum): 
    team_n=chr(ord(s)+i)
    print(f'---チーム{team_n}---')
    memList=[''] * memNum
    for j in range(0,len(memList)):
        memList[j]=allMem[j+i*memNum]
    print(memList)
    print(f'reader:{memList[0]}')
    for mem in memList:
        print(mem)
