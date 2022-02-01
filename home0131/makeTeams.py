import random

allMem=['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']

print(len(allMem))
print(allMem)
random.shuffle(allMem)
print(allMem)

teamNum=int(input("いくつチームを作りますか(1-12)?"))
memNum=int(len(allMem)/teamNum)
memNums=int(len(allMem)%teamNum)
s='A'
allCount=0

for i in range(0,teamNum): 
    team_n=chr(ord(s)+i)
    print(f'---チーム{team_n}---')
    #余りがゼロとそれ以外で場合分け
    #ゼロ以外は、余りと同じ数だけリストを作る。リストの要素はプラス１
    if memNums==0:
       memList=[''] * memNum
    else:
        if i < memNums:
           memList=[''] * (memNum+1)
        else:
           memList=[''] * memNum


    for j in range(0,len(memList)):
        memList[j]=allMem[allCount]
        allCount+=1

    print(memList)
    print(f'reader:{memList[0]}')

    for mem in memList:
        print(mem)
