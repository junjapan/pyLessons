ages=[28,50,'ひみつ',20,78,25,22,10,'無回答',33]
print(ages)
samples=list()
for data in ages:
    # javaの場合→ if (! data instanceof Integer){}
    if not isinstance(data,int):
        continue
    if data < 20 or data >= 30:
        continue
    samples.append(data)
print(samples)
