import beta_ntf
import numpy as np

# define matrix A

A = np.array([  [0, 0, 1, 0, 1, 1],
                        [1, 1, 1, 1, 0, 0],
                        [1, 1, 0, 0, 1, 1],
                    ],  np.float)

Z = np.array([  [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]
                    ],  np.float)

# Create the BetaNTF object
ntf = beta_ntf.BetaNTF(A.shape, n_components=2, beta=1, n_iter=500, verbose=False)

# Factorization
ntf.fit(A)

# A ~ X.Y
X = ntf.factors_[0]
Y = ntf.factors_[1].transpose()

# check result
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print
print A
print
print X
print
print Y
print
print np.dot(X, Y)
def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))




print dist(A, np.dot(X,Y))
print dist(A, Z)
