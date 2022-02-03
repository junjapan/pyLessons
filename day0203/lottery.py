import random
lotts=['{:04d}'.format(i) for i in range(10000)]

print(f'{10:04d}の2倍は{20:04d}')

#print(lotts)
'''
n1 = random.randint(1,6) #1-6
n2 = random.randrange(2,10) #2-9
data = ['red','green','blue']
color=random.choice(data)
print(type(color))
'''

n=int(input('宝くじを何枚買いますか？>>'))
my_lotts=sorted(random.sample(lotts,n))
#my_lotts=sorted(random.sample(lotts,n),reverse=True)
print(my_lotts)
lucky='{:04d}'.format(random.randrange(10000))
print('抽選開始...')
print(lucky[0]) #先頭の文字
for c in lucky:
    print(c)

result=[[] for i in range(4)]
for lott in my_lotts:
    if lucky == lott:
        result[0].append(lott)
    elif lucky[-3:]==lott[-3:]:
        result[1].append(lott)
    elif lucky[-2:]==lott[-2:]:
        result[2].append(lott)
    elif lucky[-1:]==lott[-1]:
        result[3].append(lott)

for i in range(len(result)):
    #*で埋める。>右詰め
    print('{}等賞({:*>4s})'.format(i+1,lucky[i:]),result[i])
