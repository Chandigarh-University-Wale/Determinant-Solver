def cofactor(L, C):
          L1=[]
          for i in range(1, len(L)):
                    for j in range(len(L)):
                              if j!=C:
                                        L1.append(L[i][j])
          L2=[L1[i:i+(int(len(L1)**0.5))] for i in range(0,len(L1),(int(len(L1)**0.5)))]
          return determinant(L2)*L[0][C]*((-1)**C)

def determinant(L):
          if len(L)==1:
                    return L[0][0]
          elif len(L)==2:
                    return L[0][0]*L[1][1] - L[0][1]*L[1][0]
          else:
                    S=0
                    for i in range(len(L)):
                              S+= cofactor(L, i)
                    return S

l=int(input('Enter the dimension of the matrix: '))
print('Enter the values of the square matrix:')
L=[[int(input()) for i in range(l)] for j in range(l)]
print('Determinant = ', determinant(L))