import numpy as np

isq2 = 1.0 / (2.0 ** 0.5)

class Qubit:
    def __init__(self):
        self.state = np.array([[1], [0]], dtype=complex)

class QuantumGate:
    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix

    def apply(self, qubits):
        raise NotImplementedError("This method should be implemented by subclasses")

class SingleQubitGate(QuantumGate):
    def apply(self, qubits, qubit_idx):
        qubits[qubit_idx].state = np.dot(self.matrix, qubits[qubit_idx].state)

class TwoQubitGate(QuantumGate):
    def apply(self, qubits, control_idx, target_idx):
        control_state = qubits[control_idx].state
        target_state = qubits[target_idx].state
        combined_state = np.kron(control_state, target_state)
        new_state = np.dot(self.matrix, combined_state)
        qubits[target_idx].state = new_state.reshape(2, 1)

class QuantumCircuit:
    def __init__(self, num_qubits):
        self.qubits = [Qubit() for _ in range(num_qubits)]
        self.gates = []

    def add_gate(self, gate, *args):
        self.gates.append((gate, args))

    def apply_gates(self):
        for gate, args in self.gates:
            gate.apply(self.qubits, *args)

    def get_states(self):
        return [qubit.state for qubit in self.qubits]

    def measure_qubit(self, qubit_idx):
        state = self.qubits[qubit_idx].state
        probabilities = np.abs(state) ** 2
        result = np.random.choice([0, 1], p=probabilities.flatten())
        return result

def main():
    gate_definitions = {
        1: SingleQubitGate("X", np.array([[0, 1], [1, 0]], dtype=complex)),
        2: SingleQubitGate("Y", np.array([[0, -1j], [1j, 0]], dtype=complex)),
        3: SingleQubitGate("Z", np.array([[1, 0], [0, -1]], dtype=complex)),
        4: SingleQubitGate("H", isq2 * np.array([[1, 1], [1, -1]], dtype=complex)),
        5: SingleQubitGate("P", np.array([[1, 0], [0, 1j]], dtype=complex)),
        6: SingleQubitGate("T", np.array([[1, 0], [0, isq2 + isq2 * 1j]], dtype=complex)),
        7: TwoQubitGate("CNOT", np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)),
        8: TwoQubitGate("CZ", np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]], dtype=complex)),
        9: TwoQubitGate("SWAP", np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)),
        10: QuantumGate("Toffoli", np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0]
        ], dtype=complex))
    }

    print("Input the number of qubits:")
    num_qubits = int(input())

    circuit = QuantumCircuit(num_qubits)

    print("Enter the first gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toffoli.")
    gate_input = int(input())

    while gate_input != 0:
        if gate_input in range(1, 7):
            print(f"Enter the qubit this gate is to be applied to (1 to {num_qubits}):")
            qubit_num = int(input()) - 1
            circuit.add_gate(gate_definitions[gate_input], qubit_num)
        elif gate_input in range(7, 10):
            print(f"Enter the control qubit (1 to {num_qubits}):")
            control_qubit = int(input()) - 1
            print(f"Enter the target qubit (1 to {num_qubits}):")
            target_qubit = int(input()) - 1
            circuit.add_gate(gate_definitions[gate_input], control_qubit, target_qubit)
        elif gate_input == 10:
            print(f"Enter the first control qubit (1 to {num_qubits}):")
            control_qubit1 = int(input()) - 1
            print(f"Enter the second control qubit (1 to {num_qubits}):")
            control_qubit2 = int(input()) - 1
            print(f"Enter the target qubit (1 to {num_qubits}):")
            target_qubit = int(input()) - 1
            circuit.add_gate(gate_definitions[gate_input], control_qubit1, control_qubit2, target_qubit)

        print("Enter the next gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toffoli.")
        gate_input = int(input())

    circuit.apply_gates()

    for idx, state in enumerate(circuit.get_states()):
        print(f"Qubit {idx + 1}: {state}")

    while True:
        print("Enter the qubit number to measure (1 to {num_qubits}), or 0 to end:")
        qubit_to_measure = int(input())
        if qubit_to_measure == 0:
            break
        elif 1 <= qubit_to_measure <= num_qubits:
            classical_state = circuit.measure_qubit(qubit_to_measure - 1)
            print(f"Classical state of Qubit {qubit_to_measure}: {classical_state}")
        else:
            print(f"Invalid qubit number. Please enter a number between 1 and {num_qubits}.")

    print("Enter any value to end program.")
    input()

if __name__ == "__main__":
    main()
