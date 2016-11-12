import string
from matplotlib import pyplot as plt

def lineChart():
	years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
	gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

	plt.plot(years, gdp, color = "red", marker = "o", linestyle = "solid")
	plt.title("Nominal GDP")
	plt.ylabel("Billions of US Dollars")
	plt.xlabel("Decades")
	plt.show()

def barChart():
	movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
	oscarCount = [5, 11, 3, 8, 10]

	#center bars
	xs = [i + 0.1 for i, _ in enumerate(movies)]

	plt.bar(xs, oscarCount)
	plt.ylabel("Number of Academy Awards")
	plt.title("Awardwinning Movies")
	#label x-axis with movie names at bar centers
	plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
	plt.show()

def lineTrend():
	variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
	biasSquared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
	totalError = [x + y for x, y in zip(variance, biasSquared)]
	xs = [i for i, _ in enumerate(variance)]

	#multiple plot calls for multiple lines on chart
	plt.plot(xs, variance, "g-", label = "Variance")
	plt.plot(xs, biasSquared, "r-.", label = "Bias^2")
	plt.plot(xs, totalError, "b:", label = "Total Error")
	plt.legend(loc = 9)
	plt.xlabel("Model Complexity")
	plt.title("The Bias-Varaiance Tradeoff")
	plt.show()

def scatterplot():
	friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
	minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
	labels = list(string.ascii_lowercase[:9])
	print(labels)

	plt.scatter(friends, minutes)

	for label, friendCount, minuteCount in zip(labels, friends, minutes):
		plt.annotate(label, xy = (friendCount, minuteCount), xytext = (5, -5), textcoords = "offset points")
	plt.title("Daily Minutes vs Number of Friends")
	plt.xlabel("Number of Friends")
	plt.ylabel("Daily Minutes Spent on Site")
	plt.show()

def main():
	lineChart()
	barChart()
	lineTrend()
	scatterplot()

if __name__ == "__main__":
	main()
