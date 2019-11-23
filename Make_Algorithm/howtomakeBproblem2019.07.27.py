a, b = input().split()
a = int(a)
b = int(b)
c = ''

Matrix = [[0]*b for i in range(a)]
Matrix_zero = [[0]*a for i in range(b)]

for i in range(a):
    c = input()
    for j in range(len(c)):
        Matrix[i][j] = c[j]

Matrix_zero = [[0]*a for i in range(b)]
for j in range(a):
    for i in range(b):
        Matrix_zero[i][j] = Matrix[j][i]

list = []
for i in range(b):
    Range = []
    for j in Matrix_zero[i]:
        if j == chr(45):
            Range.append(chr(124))
        if j == chr(124):
            Range.append(chr(45))
        if j == chr(47):
            Range.append(chr(92))
        if j == chr(92):
            Range.append(chr(47))
        if j == chr(94):
            Range.append(chr(60))
        if j == chr(60):
            Range.append(chr(118))
        if j == chr(118):
            Range.append(chr(62))
        if j == chr(62):
            Range.append(chr(94))
        if j == chr(46):
            Range.append(chr(46))
        if j == chr(79):
            Range.append(chr(79))
    list.append(Range)

for i in range(b-1, -1, -1):
    c = "".join(list[i])
    print(c)
