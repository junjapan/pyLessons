# temp=[7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
# temp_new=[]
# count=0
# sum=0
# for t in temp:
#     print(t,end=',')

#     if count == 5: 
#         temp_new.append('N/A')
#     else:
#         temp_new.append(t)
#         sum += t
#     count +=1
# print()
# for t in temp_new:
#     print(t,end=',')
# print()
# print('平均気温は{}度です'.format(sum/count))
temp=[7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
for t in temp:
    print(t,end=',')
print()
temp_new=temp[:]
temp_new[5]='N/A'
samples=[]
for t in temp_new:
    print(t,end=',')
    if not isinstance(t,float):
        continue
    samples.append(t)
print()
print(f'平均気温:{sum(samples)/len(samples)}')