from scipy.stats import binom
import matplotlib.pyplot as plt
# setting the values
# of n and p
n = 100
p = 0.5
# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph
plt.stem(r_values, dist)
plt.title("n=100")
plt.xlabel("Número de experimentos")
plt.ylabel("Probabilidad de que salga Cara")
plt.show()
