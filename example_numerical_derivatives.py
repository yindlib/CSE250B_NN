"""
Calculate derivatives numerically using finite central-differences.
"""

import numpy as np
import matplotlib.pyplot as plt


### Generate example data

# weight matrix
W = np.linspace(0, 2 * np.pi)

# grid spacing
dW = W[1] - W[0]

# objective function: J = J(W)
J = np.sin(W)


### Calculate derivatives
# NOTE: numpy's gradient function calculates derivatives using finite
# central-differences (which is what we want for project #4)
dJdW = np.gradient(J, dW)


### Plot (to visually verify gradients)
plt.figure()
ax = plt.subplot(111)

# objective function
ax.plot(W, J, label='J(W)', c='k', ls='-', lw=2)

# gradient
ax.plot(W, dJdW, label='dJ/dW', c='#268bd2', ls='--', lw=2)

ax.set_ylim([-2, 2])

ax.set_xlabel('W')

ax.legend()

plt.show()
