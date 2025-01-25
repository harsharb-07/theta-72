import statistics
import numpy as np

stock_prices = [100, 102, 98, 105, 101, 97, 99, 103, 100, 98]

variance = statistics.variance(stock_prices)
print(f"Variance of stock prices: {variance}")

numpy_variance = np.var(stock_prices, ddof=1) #ddof = 1 for sample variance
print(f"Variance of stock prices (using NumPy) : {numpy_variance}" )