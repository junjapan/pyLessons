import random

allMem=['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']

print(len(allMem))
print(allMem)
random.shuffle(allMem)
print(allMem)

teamNum=2
memNum=int(len(allMem)/teamNum)

for i in range(0,teamNum): 
    memList=[''] * memNum
    for j in range(0,len(memList)):
        memList[j]=allMem[j+i*memNum]
    print(memList)
