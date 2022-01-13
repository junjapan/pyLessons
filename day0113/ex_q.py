import pprint
q1 = [[i*10+j for j in range(10,0,-1)] for i in range(9,-1,-1)]
pprint.pprint(q1)

print("--------")

q2=[[1 if i==j or i+j == 4 else 0 for j in range(5)] for i in range(5)]
pprint.pprint(q2)

print("--------")

q3=[[i*10-j*10 for j in range(10)] for i in range(10)]
pprint.pprint(q3)

print("--------")

q4=[[ 1 if i==j else 2 if i>j else 0 for j in range(5)] for i in range(5)]
pprint.pprint(q4)

print("--------")

q5=[[ 1+i if i==j else 0 for j in range(4)] for i in range(4)]
pprint.pprint(q5)

print("--------")

q6=[[(i+6)*10+j  for j in range(9)] for i in range(4)]
pprint.pprint(q6)

print("--------")

q7=[[(j+1)*(i+1)  for j in range(9)] for i in range(9)]
pprint.pprint(q7)

print("--------")

q8=[[7 if i==j==1 else 3  for j in range(3)] for i in range(3)]
pprint.pprint(q8)

print("--------")

q9=[[ (j+1)*(i*2+3) for j in range(9)] for i in range(4)]
pprint.pprint(q9)

print("--------")

q10=[[ i+(2*j) for j in range(5)] for i in range(2,0,-1)]
pprint.pprint(q10)

print("--------")

q11=[[ '_' if j%2 != 0 and i%2 != 0 else '*' for j in range(10)] for i in range(10)]
pprint.pprint(q11)

print("--------")

q12=[[ j+(i**2) for j in range(10)] for i in range(10)]
pprint.pprint(q12)

print("--------")

q13=[[j for j in range(10-i,0,-1)] for i in range(10)]
pprint.pprint(q13)
