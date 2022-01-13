import pprint
data=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
print(data)
pprint.pprint(data)
print("------1")

W=10
H=10
data=[None]*H
for i in range(H):
    data[i]=[0]*W
data[1][1]=4
pprint.pprint(data)

print("------2")

data1=[[0]*W]*H
pprint.pprint(data1)

data1[1][1]=5
pprint.pprint(data1)

print("------3")

data2=[[0]*W for i in range(H)]
pprint.pprint(data2)

data2[1][1]=3
pprint.pprint(data2)

print("------4")

data3=[[(i*10)+j for j in range(1,11)] for i in range(W)]
pprint.pprint(data3)

print("------5")

x=[i for i in range(1,8)]
print(x)

x=[i**2 for i in range(1,8)]
print(x)

x=[i for i in range(1,8) if i%2==0]
print(x)

x=[i for i in range(2,7,2)]

x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)

x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)
