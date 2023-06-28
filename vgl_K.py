import numpy as np
import matplotlib.pyplot as plt

from market import Market
from algo import longstaff_schwartz
from scipy.stats import norm

# Parameters
T = 1
N = 1000
n = 100
degree = 5
r = 0.06
sigma = 0.2
s0 = 36

# Initialize Market
M = Market(n=n, N=N, sigma=sigma, r=r, s0=s0, T=T)
t = M.time_grid()
BB = M.brownian_motion()
Stock = M.black_scholes()
K = np.linspace(1, 100, 100)
res_value = np.zeros_like(K)  
res_theory = np.zeros_like(K)
var = np.zeros_like(K)

z = 0
for k in K:
    print(k)
    res_value[z], var[z] = longstaff_schwartz(Market=M, degree=degree, K=k, payoff="Call", regression_type="polynomial")
    d1 = (np.log(s0/k) + (r + 0.5*sigma**2)*T)
    d2 = d1 - sigma*np.sqrt(T)
    value_e = np.maximum(s0*norm.cdf(d1) - k*np.exp(-r)*norm.cdf(d2), 0)
    res_theory[z] = value_e
    z = z+1

# Visualization
plt.plot(K, res_value)
plt.plot(K, res_theory)
plt.title('LSM with '+str(N)+' MC Runs and Grid-size '+str(n)+', s0 = '+str(s0))
plt.axvline(s0, color='red')
plt.xlabel('Strike price K')
plt.ylabel('Estimated v_0')
plt.legend(['Estimated Value', 'Theoretical Value', 's0'])
plt.savefig('picture.png')
plt.show()
