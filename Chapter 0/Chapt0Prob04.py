#The normal modes and angular frequencies of those modes for a
#  linearsystem of four coupled oscillators of massm, separated by
#  springs ofequal strengthk, are given by the eigenvectors and 
# eigenvalues ofM,shown below.
# M=[2−1 0 0]
#   [−1 2 −1 0]
#   [0 −1 2 −1]
#   [0 0 −1 2]
# (The eigenvalues give the angular frequenciesωin units of√km.)
#   Findthose angular frequencies.
from matplotlib import pyplot as plt
import numpy as np

M = np.array([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]],np.int32)
#print(M)
eigenM = np.linalg.eig(M)

print('Eigenvalues of the matrix')

for i in range(len(eigenM[0])):
    print(eigenM[0][i])
