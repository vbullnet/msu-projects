'''
Created on 28 june 2016 y.

@author: vbull
'''
def binomCoeff(n,k):
    if(n==k or k==0):
        return 1
    else:
        return binomCoeff(n-1, k)+binomCoeff(n-1,k-1)
    
n=int(input())
k=int(input())

print(binomCoeff(n, k))

    