rowsize=int(input('please enter number of rows'))
if rowsize%2==0:
 Halfdiarow=int(rowsize/2)
else:
 Halfdiarow=int(rowsize/2)+1
space=Halfdiarow-1
for i in range (1,Halfdiarow+1):
 for j in range (1,space +1):
  print(end='')
 space=space-1
 number=1
 for j in range (2*i-1):
  print(end=str(number))
  number=number+1
 print()
space=1
for i in range (1,Halfdiarow):
 for j in range (1,space +1):
  print(end='')
 space=space+1
 number=1
 for j in range (1,2*(Halfdiarow-i)):
  print(end=str(number))
  number=number+1
 print()
