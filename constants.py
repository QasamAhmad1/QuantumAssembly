#making required numpy library accessible
import numpy as np

#grouping together pauli spin matrices as constants that are easily accessible
class pauli:
    x = np.array([
        [0, 1],
        [1, 0]
    ], dtype = complex)

    y = np.array([
        [0, -1j],
        [1j, 0]
    ], dtype = complex)

    z = np.array([
        [1, 0],
        [0, -1]
    ], dtype = complex)

#defining a dictionary for access to the computational basis state vectors
c2_basis = {
    "0": np.array([1 + 0j, 0 + 0j], dtype = complex),
    "1": np.array([0 + 0j, 1 + 0j], dtype = complex)
}

#definitions of remaining single qubit gates
hadamard = np.multiply(
    1 / np.sqrt(2),
    np.array([
        [1, 1],
        [1, -1]
    ], dtype = complex)
)

pi_by_8 = np.array([
    [1, 0],
    [0, np.e ** ((1j) * (np.pi / 4))]
], dtype = complex)

phase = np.array([
    [1, 0],
    [0, -1j]
], dtype = complex)
