# Pyramid pattern

rows=int(input('Rows: '))

pyramid=[]

for row in range(1,rows+1):

  st=''

  # add left spaces
  st+=' '*(rows-row)

  # add stars
  st+='*'*(2*row-1)

  # add right spaces
  st+=' '*(rows-row)

  pyramid.append(st)

print(pyramid)



# inverted pyramid

rows=int(input('Rows: '))

inverted_pyramid=[]

for row in range(rows,0,-1):

  st=''

  # add left spaces
  st+=' '*(rows-row)

  # add stars
  st+='*'*(2*row-1)

  # add right spaces
  st+=' '*(rows-row)

  inverted_pyramid.append(st)

print(inverted_pyramid)


# triangle with repeated numbers
rows=int(input('Rows: '))

triangle=[]

for row in range(1,rows+1):

  st=str(row)
  triangle.append(st*row)

print(triangle)


# Floyd's triangle

rows=int(input('Rows: '))

floyd_triangle=[]

x=1

for row in range(1,rows+1):

  st=''

  for col in range(1,row+1):
    if st=='': st+=str(x)
    else : st+=(' '+str(x))
    x+=1

  floyd_triangle.append(st)

print(floyd_triangle)

