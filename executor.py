#importing classes and constants from the constants and computer files

import parsley
import computer
from constants import hadamard, pauli, pi_by_8, phase, c2_basis


#defining the main function which catches all errors
def main():
      try:
            print(execute(input("Enter the path of your file: ")))

      except:
            print("Syntax error, please refer to the user guide.")


#applies grammar rules to every line in the user's file
def execute(filepath):
      with open(filepath) as f:
            q_code = f.read().splitlines()
            for n, content in enumerate(q_code):
                  qasm(content).expr()

      return "|psi> = |{0}>".format("".join(map(str, comp.measure())))

#catches additional errors in user input
try:
      print("--------------------- QUANTUM_ASSEMBLY ---------------------")
      number_of_qubits = int(input("Enter number of qubits: "))
      comp = computer.Computer(number_of_qubits)

except:
      print("A positive integer number of qubits is required.")
      raise TypeError("Only positive integers are allowed.")

#defines the grammar rules and functions to be applied
qasm = parsley.makeGrammar("""
number = <digit+>:ds -> int(ds)
ws = ' '*
expr = number:qubit ws ( 'H' -> apply_gate(H, qubit)
                       | 'X' -> apply_gate(X, qubit)
                       | 'Y' -> apply_gate(Y, qubit)
                       | 'Z' -> apply_gate(Z, qubit)
                       | 'E' -> apply_gate(E, qubit)
                       | 'P' -> apply_gate(P, qubit)
                       | -> 'Invalid Gate')
      | -> 'Invalid Syntax'
""", {"apply_gate": comp.apply_gate,
      "H": hadamard,
      "X": pauli.x,
      "Y": pauli.y,
      "Z": pauli.z,
      "E": pi_by_8,
      "P": phase})

if __name__ == "__main__":
      main()
