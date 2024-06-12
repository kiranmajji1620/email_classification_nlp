import numpy as np
   
   
   
matrix = np.array([
                   [0.98, 0.98, 0.98],
                   [0.98, 0.98, 0.98],
                   [0.98, 0.98, 0.98]
                   ])
                   
eigenvalues = np.linalg.eigvals(matrix)
print(eigenvalues)
