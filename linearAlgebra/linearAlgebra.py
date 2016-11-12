import functools

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


