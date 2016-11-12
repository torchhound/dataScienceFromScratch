import functools
import math

#Vectors and scalars

def vectroAdd(v, w):
	'''Adds corresponding elements'''
	return [vI + wI for vI, wI in zip(v, w)]

def vectorSub(v, w):
	'''Subtracts corresponding elements'''
	return [vI - wI for vI, wI in zip(v, w)]

def vectorSum(vectors):
	return reduce(vectorAdd, vectors)

def scalarMultiply(c, v):
	'''c is a number, v is a vector'''
	return map(lambda x: x * c, v)

def vectorMean(vectors):
	'''Compute the vector whose nth element is the mean of the nth elements of the input vectors'''
	n = len(vectors)
	return scalarMultiply(1 / n, vectorSum(vectors))

def dot(v, w):
	'''v1 * w1 + ... + vN * wN'''
	return sum(vI * wI for vI, wI in zip(v, w))

def sumOfSquares(v):
	'''v1 * v1 + ... + vN * vN'''
	return dot(v, v)

def magnitude(v):
	return math.sqrt(sumOfSquares(v))

def distance(v, w):
	return magnitude(vectorSub(v, w))

#Matrices

def shape(A):
	numRows = len(A)
	numCols = len(A[0]) if A else 0
	return numRows, numCols

def getRow(A, i):
	return A[i]

def getColumn(A, j):
	return [Ai[j] for Ai in A]

def makeMatrix(rows, cols, entry):
	return [[entry(i, j) for j in range(cols)] for i in range(rows)]

def isDiagonal(i, j):
	return 1 if i == j else 0
