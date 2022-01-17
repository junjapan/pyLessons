x=['ABC']
y=[input()]
print(id(x))
print(id(y))
print(x[0]==y[0])
print(id(x[0])==id(y[0]))

y=x
y[0]='XYZ'
print(x[0])
