print('Mirrored Half Pyramid')
n = int(input('Please enter number of rows'))
for i in range(n):
    for j in range(n - i - 1):  
        print(' ', end='')
    for j in range(i + 1): 
        print('m', end='')
    print()  

