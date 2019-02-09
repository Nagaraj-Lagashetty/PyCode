rows = input('enter No. of rows')
print(rows)
n = 1
while n <= (int(rows)):
    print('*'*n)
    n += 1

print('--------------------')

for i in range(1,int(rows)+1):
    for j in range(1,i+1):
        print('*',end='')
    print()