from __future__ import division

def mean(x):
	return sum(x) / len(x)

def median(x):
	n = len(x)
	sortedX = sorted(x)
	midpoint = n // 2

	if n % 2 == 1:
		return sortedX[midpoint]
	else:
		low = midpoint - 1
		high = midpoint
		return (sortedX[low] + sortedX[high]) / 2

def quantile(x, p):
	'''Returns the pth-percentile value in x, generalization of median'''
	pIndex = int(p * len(x))
	return sorted(x)[pIndex]

def mode(x):
	counts = Counter(x)
	maxCount = max(counts.values())
	return [xI for xI, count in counts.iteritems() if count == maxCount]

def dataRange(x):
	return max(x) - min(x)

def deMean(x):
	'''Translate x by subtracting its mean'''
	return [xI - mean(x) for xI in x]

def dot(v, w):
	return sum(vI * wI for vI, wI in zip(v, w))

def sumOfSquares(v):
	return dot(v, v)

def variance(x):
	'''For x of length two or greater'''
	deviations = deMean(x)
	return sumOfSquares(deviations) / (len(x) - 1)

def standardDeviation(x):
	return math.sqrt(variance(x))

def interquartilRange(x):
	'''Difference between 75th percentile and 25th percentile'''
	return quartile(x, 0.75) - quartile(x, 0.25)

def covariance(x, y):
	n = len(x)
	return dot(deMean(x), deMean(y)) / (n - 1)

def correlation(x, y):
	stdevX = standardDeviation(x)
	stdevY = standardDeviation(y)
	if stdevX > 0 and stdevY > 0:
		return covariance(x, y) / stdevX / stdevY
	else:
		return 0
