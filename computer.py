#!/usr/bin/env python3

#importing required functions and constants from libraries and constants file
from functools import reduce

from constants import hadamard, pauli, pi_by_8, phase, c2_basis
import numpy as np


#function that returns list of binary digits
# e.g. 3 -> [1, 1]
def binary_digits(num):
    binary = bin(num)
    return [int(i) for i in binary[2:]]


#function that pads an array with leading 0s to a specified length
# e.g. [1, 1, 1], 5 -> [0, 0, 1, 1, 1]
def zero_pad(arr, size):
    return [0] * (size - len(arr)) + arr


class Computer:

    #class constuctor assigning attributes and initial state of the object
    def __init__(self, qubits):
        self._qubits = qubits

        self._state = np.zeros(2 ** self._qubits, dtype = complex)
        self._state[0] = 1 + 0j


    #quantum logic gate generator for systems of specifc size
    def _generate_gate(self, single_qubit_matrix, qubit_idx):
        pureStates = np.zeros(2 ** self._qubits)
        transformationMatrix = np.zeros((2 ** self._qubits, 2 ** self._qubits), dtype = complex)

        for stateNumber, state_vector in enumerate(pureStates):
            state_vector = zero_pad(binary_digits(stateNumber), self._qubits)
            count = 0

            while count < len(state_vector):
                state_vector[count] = c2_basis[str(state_vector[count])]
                count += 1

            state_vector[qubit_idx - 1] = single_qubit_matrix.dot(state_vector[qubit_idx - 1])

            transformedState = reduce(np.kron, state_vector)
            transformationMatrix[stateNumber] = transformedState

        return transformationMatrix.transpose()


    #applies the gate from the generation function to the state of the system by calculating the
    #matrix product
    def apply_gate(self, single_qubit_matrix, qubit_idx):
        state = self._state
        gate = self._generate_gate(single_qubit_matrix, qubit_idx)
        self._state = np.matmul(gate, state.transpose())


    #generates a non-uniform probability distribution and takes a sample from it
    def measure(self):
        probabilities = [abs(z) ** 2 for z in self._state]
        count = 0
        possibilities = np.zeros(2 ** (self._qubits), dtype = int)

        while count < len(possibilities):
            possibilities[count] = count
            count += 1

        decimal = np.random.choice(possibilities, p = probabilities)

        return zero_pad(binary_digits(decimal), self._qubits)
