import numpy as np
import numpy.linalg as la

def pageRank(linkMatrix, d) :
    n = linkMatrix.shape[0]
    M = d * linkMatrix + (1-d)/n * np.ones([n, n])
    r = 100 * np.ones(n) / n
    
    lastR = r
    r = M @ r
    
    while la.norm(lastR - r) > 0.01:
        lastR = r
        r = M @ r
    
    return r
