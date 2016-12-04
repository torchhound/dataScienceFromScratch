import math
from matplotlib import pyplot as plt

def uniformPdf(x):
	return 1 if x >= 0 and x < 1 else 0

def uniformCdf(x):
	if x < 0:
		return 0
	elif x < 1:
		return x
	else:
		return 1

def normalPdf(x, mu = 0, sigma = 1):
	sqrtTwoPi = math.sqrt(2 * math.pi)
	return (math.exp(-(x - mu) ** 2 / 2 /sigma ** 2) / (sqrtTwoPi * sigma))

def plotNormalPdfs():
	xs = [x / 10.0 for x in range(-50, 50)]
	plt.plot(xs, [normalPdf(x, sigma = 1) for x in xs], "-", label = "mu = 0, sigma = 1")
	plt.plot(xs, [normalPdf(x, sigma = 2) for x in xs], "--", label = "mu = 0, sigma = 2")
	plt.plot(xs, [normalPdf(x, sigma = 0.5) for x in xs], ":", label = "mu = 0, sigma = 0.5")
	plt.plot(xs, [normalPdf(x, mu = -1) for x in xs], "-.", label = "mu = -1, sigma = 1")
	plt.legend()
	plt.title("Various Normal Probability Density Functions")
	plt.show()

plotNormalPdfs()

def normalCdf(x, mu = 0, sigma = 1):
	return (1 + math.erf((x - mu) / math.sqrt(2) /sigma)) / 2
