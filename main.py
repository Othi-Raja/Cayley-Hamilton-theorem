import numpy as p
import  math

a = p.array([[5, 4], [1, 2]])
print("The given question",a)
S1 = a[0, 0] + a[1, 1] # 7
S2 = a[0, 0] *a[1,1]-a[0,1]*a[1,0]# 6
# to verify A^2 - S!A+ S2I
# to find A^2
row1_col1 = a[0, 0] * a[0, 0] + a[0, 1] * a[1, 0]  # 29
row1_col2 = a[0, 0] * a[0, 1] + a[0, 1] * a[1, 1]  # 28
row2_col1 = a[1, 0] * a[0, 0] + a[1, 1] * a[1, 0]  # 7
row2_col2 = a[1, 0] * a[0, 1] + a[1, 1] * a[1, 1]  # 8
ar = p.array([row1_col1, row1_col2, row2_col1, row2_col2])
shape = ar.reshape(2, 2)  # [[29 28]
# [ 7  8]]
# to verify A^2- S1A+ S2I
# to find -S1A
ar1=p.array([1,0,0,1])
I=ar1.reshape(2,2)
LHS=  shape-S1*a+S2*I
print("A^2-S1A+ S2I/RHS=",LHS)

#A inverse
A1=1//S2*S1*I-a
b=1/S2
print(b)

