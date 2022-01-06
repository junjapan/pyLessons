numbers=[1,1]
ratios=[]
ratio=0
while True:
    add = numbers[len(numbers)-1] + numbers[len(numbers)-2]
    if add < 1000:
       numbers.append(add)
       ratio = add/numbers[len(numbers)-2]
       ratios.append(ratio)
    else:
       break
print('ratios mae:'+str(ratios))
print('numbers:'+str(numbers))
for n in range(len(ratios)):
    ratios[n] = int(ratios[n]*1000)/1000
print('ratios ato:'+str(ratios))
